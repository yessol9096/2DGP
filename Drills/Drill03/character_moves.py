from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here

x = 400
y = 50
dir = 'right'
while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    if(dir == 'right'):
        x = x + 2
        y = 50
        if ( x > 750):
            dir = 'up'
        elif(x == 350):
            dir = 'circle'
    elif ( dir == 'up' ):
        y = y + 2
        if( y > 550):
            dir = 'left'
    elif ( dir == 'left' ):
        x = x - 2
        if( x < 50 ):
            dir = 'down'
    elif ( dir == 'down' ):
        y = y - 2
        if (y < 50):
            dir = 'right'
    elif (dir == 'circle'):
        for i in range(1, 360):
            clear_canvas_now()
            grass.draw_now(400, 30)
            r = (360-i) * math.pi / 180
            x = 400 + 200 * math.cos(r)
            y = 300 + 200 * math.sin(r)
            character.draw_now(x, y)
        dir = 'right'
        x = 400
        
    character.draw_now(x, y)
    delay(0.01)
close_canvas()
