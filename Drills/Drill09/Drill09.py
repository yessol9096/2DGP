from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
class Small_Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100,700), 599
        self.speed = random.randint(5,20)
    def update(self):
        if(self.y > 50):
            self.y -= self.speed
    def draw(self):
        self.image.draw(self.x, self.y)

class Big_Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100,700), 599
        self.speed = random.randint(3,20)

    def update(self):
        if(self.y > 50):
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


open_canvas()


grass = Grass()

running = True

team = [Boy() for i in range(11)]
small_num = random.randint(1,19)
bid_num = 20 - small_num
Small_Ball = [Small_Ball() for i in range(small_num)]
Big_Ball = [Big_Ball() for i in range(bid_num)]
ball_speed = 0
while running:
    for boy in team:
        boy.update()


    for smallball in Small_Ball:
        smallball.update()


    for bigball in Big_Ball:
        bigball.update()


    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for smallball in Small_Ball:
        smallball.draw()
    for bigball in Big_Ball:
        bigball.draw()
    update_canvas()

    delay(0.05)

close_canvas()

#완성