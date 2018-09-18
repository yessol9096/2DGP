from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def go_to(sx, sy, ex, ey):
    if (sx < ex and sy < ey):
        move_right_up(sx, sy, ex, ey)
    elif (sx < ex and sy > ey):
        move_right_down(sx, sy, ex, ey)
    elif (sx > ex and sy < ey):
        move_left_up(sx, sy, ex, ey)
    elif (sx > ex and sy > ey):
        move_left_down(sx, sy, ex, ey)
    pass

def move_right_up(sx, sy, ex, ey):
    frame = 0
    while True:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, sx, sy)
        update_canvas()
        frame = (frame + 1) % 8
        if(sx < ex):
            sx += 2
        if(sy < ey):
            sy += 2
        delay(0.01)
        if(sx > ex and sy > ey):
            break;
    delay(0.05)
    get_events()
    pass
def move_right_down(sx, sy, ex, ey):
    frame = 0
    while True:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, sx, sy)
        update_canvas()
        frame = (frame + 1) % 8
        if (sx < ex):
            sx += 2
        if (sy > ey):
            sy -= 2
        delay(0.01)
        if (sx > ex and sy < ey):
            break;
    delay(0.05)
    get_events()
    pass
def move_left_up(sx, sy, ex, ey):
    pass
def move_left_down(sx, sy, ex, ey):
    pass

while True:
    move_right_down(132, 243, 535, 100)
    #go_to(203, 535, 132, 243)
    #go_to(132, 243, 535, 470)
    #go_to(535, 470, 477, 203)
    #go_to(477, 203, 715, 136)
    #go_to(715, 136, 316, 225)
    #go_to(316, 255, 510, 92)
    #go_to(510, 92, 692, 518)
    #go_to(692, 518, 682, 336)
    #go_to(682, 336, 712, 349)
    #go_to(712, 349, 203, 535)
close_canvas()

