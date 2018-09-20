from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global x, y
    global movex, movey
    global mousex, mousey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mousex, mousey = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



# fill here
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
movex = KPU_WIDTH // 2
movey =  KPU_HEIGHT // 2
mousex = KPU_WIDTH // 2
mousey =  KPU_HEIGHT // 2
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x, y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, movex, movey)
    if(mousex > movex):
        movex += 1
    if (mousex < movex):
        movex -= 1
    if (mousey > movey):
        movey += 1
    if (mousey < movey):
        movey -= 1
    update_canvas()
    frame = (frame + 1) % 8
    hide_cursor()
    delay(0.02)
    handle_events()

close_canvas()




