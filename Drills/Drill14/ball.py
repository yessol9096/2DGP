import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None


    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0,800), 0

    def get_bb(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def draw(self):
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        self.x = clamp(0, self.x, self.bg.w)
        self.y = clamp(70, self.y, 1110)
        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom

    def set_background(self, bg):
        self.bg = bg

