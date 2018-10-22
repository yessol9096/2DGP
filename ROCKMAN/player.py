import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import advanced_pause_state

# png 이미지 가로 6 * 40 세로 7 * 40

name = "MainState"

player = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Player:
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
        if (dir == 1):
            self.frame_y = 6
        elif (dir == -1) :
            self.frame_y = 5

    def walk(self):
        self.frame_update()
        self.x += (self.dir) * self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 40,  self.frame_y * 40, 40, 40, self.x , self.y)


def enter():
    global player, grass
    player = Player()
    grass = Grass()


def exit():
    global player, grass
    del(player)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            player.dir = 1
            player.walk()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            player.dir = -1
            player.walk()





def update():
    player.update()


def draw():
    clear_canvas()
    grass.draw()
    player.draw()
    update_canvas()






