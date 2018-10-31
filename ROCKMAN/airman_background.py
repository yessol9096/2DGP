from pico2d import *

class Airman_background:
    def __init__(self):
        self.image = load_image('resource/stage/AirManMapBG.png')
        self.canvas_width = 800
        self.canvas_height = 700
        self.w = self.image.w
        self.h = self.image.h
    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_width//2,
                                 self.h - self.canvas_height)

    def draw(self):
        self.image.clip_draw_to_origin(0,483,254,237,400,350,self.canvas_width, self.canvas_height)

    def set_center_object(self, player):
        self.center_object = player


