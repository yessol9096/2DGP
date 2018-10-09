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
        self.x, self.y = random.randint(100,700), random.randint(600, 2000)
        self.speed = random.randint(1,20)
    def update(self):
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
Small_Ball = [Small_Ball() for i in range(10)]

while running:
    for boy in team:
        boy.update()

    for smallball in Small_Ball:
        smallball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for smallball in Small_Ball:
        smallball.draw()
    update_canvas()

    delay(0.05)

close_canvas()
