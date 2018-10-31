import game_framework
import pico2d

import start_state
import pause_state
import advanced_pause_state
import airman_stage
import rockman
pico2d.open_canvas()
game_framework.run(airman_stage)
pico2d.close_canvas()
# fill here
