from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
def draw_line(p1, p2):
    frame = 0
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    hide_cursor()
    delay(0.05)
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 20
points = [(random.randint(100, 1180), random.randint(100, 980)) for i in range(size)]
n = 1
while(1) :
    draw_line(points[n-1],points[n])
    n = (n + 1) % size


turtle.done()