from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
def draw_line(p1, p2):
    frame = 0
    dir = 0
    if(p1[0] - p2[0] > 0) :
        dir = 0
    elif(p1[0] - p2[0] < 0)  :
        dir = 1
    elif (p1[0] == p2[0]):
        pass
    for i in range(0, 100 + 1, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
# 완성
size = 20
points = [(random.randint(150, 1180), random.randint(150, 980)) for i in range(size)]
n = 1

while(1) :
    draw_line(points[n-1],points[n])
    n = (n + 1) % size
