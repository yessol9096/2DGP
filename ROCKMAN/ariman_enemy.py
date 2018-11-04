from pico2d import *
import game_framework
import game_world

TIME_PER_ACTION = 1   # 한번 액션하는데 0.5 걸린다
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION    # 시간당 몇번 액션 할 것인가
FRAMES_PER_ACTION = 8

class Tikky:

    def __init__(self):
        self.image = load_image('resource/enemy/Tikky.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = 0
        self.left = 0
        self.bottom = 483

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 15

    def draw(self):
        self.image.clip_draw(self.left, int(self.frame) * 104, 80, 104, 400, 350, 200, 250)


