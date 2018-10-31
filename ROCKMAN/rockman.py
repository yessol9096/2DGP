import game_framework
from pico2d import *
from bullet import Bullet
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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, ATTACK, ATTACK_OFF, JUMP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_z): ATTACK,
    (SDL_KEYUP, SDLK_z): ATTACK_OFF,
    (SDL_KEYDOWN, SDLK_x): JUMP
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
        pass

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3


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
        pass

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


class Idle_attackState:

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
        rockman.frame = 0
        rockman.attack()

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        rockman.x = clamp(25, rockman.x, 1600 - 25)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(0, 160, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(0, 120, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)

class Run_attackState:

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

        rockman.attack()

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(25, rockman.x, 1600 - 25)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 160, 40, 40, rockman.x, rockman.y, CHAR_SIZE,
                                    CHAR_SIZE)
        else:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 120, 40, 40, rockman.x, rockman.y, CHAR_SIZE,
                                    CHAR_SIZE)

class JumpState:
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
        rockman.frame = 0

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def jump(rockman):
        gap_time = 0.1
        game_framework.frame_time

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(25, rockman.x, 1600 - 25)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(160, 240, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(160, 200, 40, 40, rockman.x, rockman.y, CHAR_SIZE, CHAR_SIZE)








next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState, ATTACK: Idle_attackState, ATTACK_OFF: IdleState, JUMP: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: RunState, ATTACK: Run_attackState, ATTACK_OFF: RunState},
    Idle_attackState: {RIGHT_UP: Idle_attackState, LEFT_UP: Idle_attackState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, ATTACK_OFF: IdleState,ATTACK: Idle_attackState},
    Run_attackState: {RIGHT_UP: Idle_attackState, LEFT_UP: Idle_attackState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, ATTACK_OFF: RunState, ATTACK: Run_attackState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, ATTACK: JumpState, ATTACK_OFF: JumpState, JUMP: JumpState}
}

class Rockman:

    def __init__(self):
        self.x, self.y = 800 // 2, 350
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('resource/rockman/rockman240x280.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.canvas_width = 800
        self.canvas_height = 700
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def set_background(self, bg):
        self.bg = bg

    def attack(self):
        bullet = Bullet(self.x, self.y, self.dir)
        game_world.add_object(bullet, 1)

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
        #self.x = clamp(0, self.x, self.bg.w)
        #self.y = clamp(0, self.y, self.bg.h)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

