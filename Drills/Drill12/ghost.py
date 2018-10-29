from pico2d import *
import game_world
import math
PIXEL_PER_METER = (10.0 / 0.3)

class Ghost:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y, self.velocity = x, y, velocity
        global boy_x, boy_y
        boy_x, boy_y = x, y
    def draw(self):
        self.image.clip_draw(0 * 100, 100, 100, 100, self.x, self.y)

    def update(self):
        global boy_x, boy_y
        #circle

        r = (360 - get_time()) * math.pi / 180
        self.x = boy_x + 3* PIXEL_PER_METER  * math.cos(r)
        self.y = boy_y + 3* PIXEL_PER_METER  * math.sin(r)
