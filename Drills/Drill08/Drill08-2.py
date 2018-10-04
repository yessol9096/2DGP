from pico2d import *
import random
import turtle

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def draw_big_point(p1, dir):
    character.clip_draw(1 * 100, 100 * dir, 100, 100, p1[0], p1[1])

def draw_curve_10_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    frame = 0
    # 1-2
    dir = 0
    dir1 = 0
    dir2 = 0
    dir3 = 0
    dir4 = 0
    dir5 = 0
    dir6 = 0
    dir7 = 0
    dir8 = 0
    dir9 = 0
    dir10 = 0
    for i in range(0, 50, 2):
        t = i / 100
        if (p1[0] - p2[0] > 0):
            dir = 0
        elif (p1[0] - p2[0] < 0):
            dir = 1
        elif (p1[0] == p2[0]):
            pass
        dir1 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 2-3
    for i in range(0, 100, 2):
        t = i / 100
        if (p2[0] - p3[0] > 0):
            dir = 0
        elif (p2[0] - p3[0] < 0):
            dir = 1
        elif (p2[0] == p3[0]):
            pass
        dir2= dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1,dir1)
        draw_big_point(p2, dir2)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 3-4
    for i in range(0, 100, 2):
        t = i / 100
        if (p3[0] - p4[0] > 0):
            dir = 0
        elif (p3[0] - p4[0] < 0):
            dir = 1
        elif (p3[0] == p4[0]):
            pass
        dir3 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 4-5
    for i in range(0, 100, 2):
        t = i / 100
        if (p4[0] - p5[0] > 0):
            dir = 0
        elif (p4[0] - p5[0] < 0):
            dir = 1
        elif (p4[0] == p5[0]):
            pass
        dir4 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 5-6
    for i in range(0, 100, 2):
        t = i / 100
        if (p5[0] - p6[0] > 0):
            dir = 0
        elif (p5[0] - p6[0] < 0):
            dir = 1
        elif (p5[0] == p6[0]):
            pass
        dir5= dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        draw_big_point(p5, dir5)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 6-7
    for i in range(0, 100, 2):
        t = i / 100
        if (p6[0] - p7[0] > 0):
            dir = 0
        elif (p6[0] - p7[0] < 0):
            dir = 1
        elif (p6[0] == p7[0]):
            pass
        dir6 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        draw_big_point(p5, dir5)
        draw_big_point(p6, dir6)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 7-8
    for i in range(0, 100, 2):
        t = i / 100
        if (p7[0] - p8[0] > 0):
            dir = 0
        elif (p7[0] - p8[0] < 0):
            dir = 1
        elif (p7[0] == p8[0]):
            pass
        dir7 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        draw_big_point(p5, dir5)
        draw_big_point(p6, dir6)
        draw_big_point(p7, dir7)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 8-9
    for i in range(0, 100, 2):
        t = i / 100
        if (p8[0] - p9[0] > 0):
            dir = 0
        elif (p8[0] - p9[0] < 0):
            dir = 1
        elif (p8[0] == p9[0]):
            pass
        dir8 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        draw_big_point(p5, dir5)
        draw_big_point(p6, dir6)
        draw_big_point(p7, dir7)
        draw_big_point(p8, dir8)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
        # 9-10
    for i in range(0, 100, 2):
        t = i / 100
        if (p9[0] - p10[0] > 0):
            dir = 0
        elif (p9[0] - p10[0] < 0):
            dir = 1
        elif (p9[0] == p10[0]):
            pass
        dir9 = dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        draw_big_point(p5, dir5)
        draw_big_point(p6, dir6)
        draw_big_point(p7, dir7)
        draw_big_point(p8, dir8)
        draw_big_point(p9, dir9)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        hide_cursor()
        delay(0.05)
    # 9-10
    for i in range(0, 100, 2):
        t = i / 100
        if (p10[0] - p1[0] > 0):
            dir = 0
        elif (p10[0] - p1[0] < 0):
            dir = 1
        elif (p10[0] == p1[0]):
            pass
        dir10 =  dir
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        draw_big_point(p1, dir1)
        draw_big_point(p2, dir2)
        draw_big_point(p3, dir3)
        draw_big_point(p4, dir4)
        draw_big_point(p5, dir5)
        draw_big_point(p6, dir6)
        draw_big_point(p7, dir7)
        draw_big_point(p8, dir8)
        draw_big_point(p9, dir9)
        draw_big_point(p10, dir10)
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
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
points = [(random.randint(150, 1000), random.randint(250, 900)) for i in range(size)]

while running:
    draw_curve_10_points((points[0]),(points[1]),(points[2]),(points[3]),
    (points[4]),(points[5]),(points[6]),(points[7]),(points[8]),(points[9]))


close_canvas()




