import random
import json
import os

from pico2d import *
import game_framework
import title_state
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5   # 한번 액션하는데 0.5 걸린다
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION    # 시간당 몇번 액션 할 것인가
FRAMES_PER_ACTION = 3

# png 이미지 가로 6 * 40 세로 7 * 40

name = "Rockman"

font = None

#Rockman event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

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


    @staticmethod
    def exit(rockman, event):
        if event == SPACE:
            rockman.fire_ball()
        pass

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(int(rockman.frame) * 100, 300, 100, 100, rockman.x, rockman.y)
        else:
            rockman.image.clip_draw(int(rockman.frame) * 100, 200, 100, 100, rockman.x, rockman.y)


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
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(25, rockman.x, 1600 - 25)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(int(rockman.frame) * 100, 100, 100, 100, rockman.x, rockman.y)
        else:
            rockman.image.clip_draw(int(rockman.frame) * 100, 0, 100, 100, rockman.x, rockman.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState}
}

class Rockman:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('resource/rockman/rockman240x280.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def frame_update(self):
        self.frame = (self.frame + 1) % 3 + 1

    def walk(self):
        self.frame_update()
        self.x += (self.dir) * self.speed

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)






