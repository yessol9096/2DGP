import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import advanced_pause_state
import game_world

# png 이미지 가로 6 * 40 세로 7 * 40

name = "Rockman"

font = None

#Rockman event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, DASH_DOWN, DASH_UP = range(8)


class Rockman:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.frame_y = 6
        self.image = load_image('resource/rockman/rockman240x280.png')
        self.dir = 1
        self.speed = 1

    def update(self):
        pass

    def frame_update(self):
        self.frame = (self.frame + 1) % 3 + 1

    def walk(self):
        self.frame_update()
        self.x += (self.dir) * self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 40,  self.frame_y * 40, 40, 40, self.x , self.y, 150, 150)
        print(self.dir)

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                self.dir = 1
                self.frame_y = 6
                self.walk()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                self.dir = -1
                self.frame_y = 5
                self.walk()






