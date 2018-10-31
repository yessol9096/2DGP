from pico2d import *

class Airman_background:
    def __init__(self):
        self.image = load_image('resource/stage/AirManMapBG.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,483,254,237,400,350,800,700)
