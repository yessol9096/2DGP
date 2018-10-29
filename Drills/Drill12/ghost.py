from pico2d import *
import game_framework
import game_world
import math
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 360 * 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
class Ghost:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        global boy_x, boy_y, init_time, wake_up
        wake_up = True
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.opacity = 0.5
        init_time = get_time()
        boy_x, boy_y = x, y
    def draw(self):
        self.image.opacify(self.opacity)
        self.image.clip_draw(0 * 100, 100, 100, 100, self.x, self.y)

    def update(self):
        global boy_x, boy_y, init_time, wake_up
        if (wake_up == True):
            self.y += 0.5
            if(self.y > 200) :
                wake_up=False
        elif (wake_up == False):
        #circle
            self.velocity = (ACTION_PER_TIME * game_framework.frame_time)
            r = (360*2 / self.velocity) * math.pi / 180
            self.x = boy_x + 3* PIXEL_PER_METER * math.cos(r)
            self.y = boy_y + 3* PIXEL_PER_METER * math.sin(r)
