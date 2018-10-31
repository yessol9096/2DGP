import random
import json
import os

from pico2d import *

import game_framework
import title_state
import airman_stage

name = "MainState"

pause_image = None


class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw_now(400, 300, 200, 200)


def enter():
    global pause_image
    pause_image = Pause()


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    pass


twinkling = 1
def draw():
    global twinkling
    clear_canvas()

    airman_stage.grass.draw()
    airman_stage.boy.draw()
    if (twinkling > 1.0):
        twinkling = 0
        pause_image.draw()
        delay(1.0)
    twinkling += 0.01
    update_canvas()









