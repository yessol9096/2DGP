import game_framework
from pico2d import *
from ball import Ball
from ghost import Ghost
import game_world

# Rockman Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

CHAR_SIZE = 120

# Rockman Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5   # 한번 액션하는데 0.5 걸린다
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION    # 시간당 몇번 액션 할 것인가
FRAMES_PER_ACTION = 5



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(rockman, event):
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS
        rockman.timer = get_time()

    @staticmethod
    def exit(rockman, event):
        if event == SPACE:
            rockman.fire_ball()
        pass

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if rockman.timer + 10.0 <= get_time():
            rockman.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(0, 240, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(0, 200, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)


class RunState:

    @staticmethod
    def enter(rockman, event):
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS
        rockman.dir = clamp(-1, rockman.velocity, 1)

    @staticmethod
    def exit(rockman, event):
        if event == SPACE:
            rockman.fire_ball()

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(25, rockman.x, 1600 - 25)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 240, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 200, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)


class SleepState:

    @staticmethod
    def enter(rockman, event):
        rockman.frame = 0
        rockman.ghost()

    @staticmethod
    def exit(rockman, event):
        rockman.delete_ghost()

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_composite_draw(int(rockman.frame) * 100, 100, 100, 100, 3.141592 / 2, '', rockman.x - 25, rockman.y - 25, 100, 100)
        else:
            rockman.image.clip_composite_draw(int(rockman.frame) * 100, 0, 100, 100, -3.141592 / 2, '', rockman.x + 25, rockman.y - 25, 100, 100)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Rockman:

    def __init__(self):
        self.x, self.y = 800 // 2, 350
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('resource/rockman/rockman240x280.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

    def ghost(self):
        global ghost
        ghost = Ghost(self.x, self.y, self.dir*3)
        game_world.add_object(ghost, 1)

    def delete_ghost(self):
        global ghost
        game_world.remove_object(ghost)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255,255,0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

