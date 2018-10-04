from pico2d import *
import random
import turtle

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    character.clip_draw(100, 100 * 1, 100, 100, p1[0], p1[1])
    character.clip_draw(100, 100 * 1, 100, 100, p2[0], p2[1])
    character.clip_draw(100, 100 * 1, 100, 100, p3[0], p3[1])
    character.clip_draw(100, 100 * 1, 100, 100, p4[0], p4[1])
    character.clip_draw(100, 100 * 1, 100, 100, p5[0], p5[1])
    character.clip_draw(100, 100 * 1, 100, 100, p6[0], p6[1])
    character.clip_draw(100, 100 * 1, 100, 100, p7[0], p7[1])
    character.clip_draw(100, 100 * 1, 100, 100, p8[0], p8[1])
    character.clip_draw(100, 100 * 1, 100, 100, p9[0], p9[1])
    character.clip_draw(100, 100 * 1, 100, 100, p10[0], p10[1])
def draw_curve_10_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    frame = 0

    for i in range(0, 50, 2):
        t = i / 100
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
    for i in range(0, 100, 2):
        t = i / 100
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
    for i in range(0, 100, 2):
        t = i / 100
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
    for i in range(0, 100, 2):
        t = i / 100
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
    for i in range(0, 100, 2):
        t = i / 100
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
    for i in range(0, 50, 2):
        t = i / 100
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        x = (2 * t ** 2 - 3 * t + 1) * p5[0] + (-4 * t ** 2 + 4 * t) * p6[0] + (2 * t ** 2 - t) * p7[0]
        y = (2 * t ** 2 - 3 * t + 1) * p5[1] + (-4 * t ** 2 + 4 * t) * p6[1] + (2 * t ** 2 - t) * p7[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)

# fill here
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2


size = 10
points = [(random.randint(100, 1180), random.randint(100, 980)) for i in range(size)]

while running:
    draw_curve_10_points((points[0]),(points[1]),(points[2]),(points[3]),
    (points[4]),(points[5]),(points[6]),(points[7]),(points[8]),(points[9]))


close_canvas()




