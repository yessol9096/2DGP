import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state


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


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    pause_image.draw()
    update_canvas()






