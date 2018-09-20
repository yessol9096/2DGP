from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running
    global cursor_x, cursor_y
    global mouse_x, mouse_y
    global Click
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursor_x, cursor_y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.type == SDL_MOUSEMOTION:
            Click = 1
            mouse_x, mouse_y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0

def go_to(sx, sy, ex, ey):
    if (sx < ex and sy < ey):
        move_right_up(sx, sy, ex, ey)
    if (sx < ex and sy > ey):
        move_right_down(sx, sy, ex, ey)
    if (sx > ex and sy < ey):
        move_left_up(sx, sy, ex, ey)
    if (sx > ex and sy > ey):
        move_left_down(sx, sy, ex, ey)



def move_right_up(sx, sy, ex, ey):
    frame = 0
    while True:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, sx, sy)
        update_canvas()
        frame = (frame + 1) % 8
        if(sx < ex):
            sx += 2
        if(sy < ey):
            sy += 2
        delay(0.01)
        if((sx > ex or sx == ex) and (sy > ey or sy == ey)):
            break
    delay(0.05)
    get_events()

def move_right_down(sx, sy, ex, ey):
    frame = 0
    while True:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, sx, sy)
        update_canvas()
        frame = (frame + 1) % 8
        if (sx < ex):
            sx += 2
        if (sy > ey):
            sy -= 2
        delay(0.01)
        if ((sx > ex or sx == ex)and (sy < ey or sy == ey)):
            break
    delay(0.05)
    get_events()
def move_left_up(sx, sy, ex, ey):
    frame = 0
    while True:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 0, 100, 100, sx, sy)
        update_canvas()
        frame = (frame + 1) % 8
        if (sx > ex):
            sx -= 2
        if (sy < ey):
            sy += 2
        delay(0.01)
        if ((sx < ex or sx == ex)and (sy > ey or sy == ey)):
            break
    delay(0.05)
    get_events()

def move_left_down(sx, sy, ex, ey):
    frame = 0
    while True:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 0, 100, 100, sx, sy)
        update_canvas()
        frame = (frame + 1) % 8
        if (sx > ex):
            sx -= 2
        if (sy > ey):
            sy -= 2
        delay(0.01)
        if ((sx < ex or sx == ex)and (sy < ey or sy == ey)):
            break
    delay(0.05)
    get_events()

def draw_cursor():
    pass
# fill here
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
Click = 0




while running:
    if(Click):
        go_to()

close_canvas()




