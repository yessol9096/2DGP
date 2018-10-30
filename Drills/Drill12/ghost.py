from pico2d import *
import game_framework
import random
import game_world
import math
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_CIRCLE = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_CIRCLE
FRAMES_PER_DEGREE = 360

TIME_PER_ACTION = 0.5   # 한번 액션하는데 0.5 걸린다
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION    # 시간당 몇번 액션 할 것인가
FRAMES_PER_ACTION = 8

class Ghost:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        global boy_x, boy_y, init_time, wake_up, mid_x
        wake_up = True
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.frame = 0
        self.scale = 10
        self.x, self.y, self.velocity = x, y, velocity
        mid_x = self.x
        self.opacity = 0.5
        init_time = get_time()
        boy_x, boy_y = x, y

    def draw(self):
        self.image.opacify(self.opacity)
        #self.image.scale(self.scale)
        self.image.scale(10)
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)

    def update(self):
        global boy_x, boy_y, init_time, wake_up, mid_x
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.opacity = random.randrange(0,10) * 0.1


        # separate
        if (wake_up == True):
            self.y += 0.5
            if(self.x < mid_x):
                self.x += 10.0
            else :
                self.x -= 10.0
            if(self.y > 200) :
                wake_up=False
        elif (wake_up == False):
        #circle
            self.velocity += (FRAMES_PER_DEGREE * ACTION_PER_TIME * game_framework.frame_time)
            r = (self.velocity) * math.pi / 180
            self.x = boy_x + 3* PIXEL_PER_METER * math.cos(r)
            self.y = boy_y + 3* PIXEL_PER_METER * math.sin(r)
