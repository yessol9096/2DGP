from pico2d import *
from rockman import Rockman
import advanced_pause_state
import game_framework
import game_world
import title_state

name = "MainState"

player = None

font = None

grass = None


def enter():
    global player, grass
    player = Rockman()
    game_world.add_object(player, 1)


def exit():
    game_world.clear()


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
                game_framework.quit()
        else:
            player.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






