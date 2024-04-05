from cs1robots import *

load_world("worlds/harvest3.wld")

hubo = Robot(beepers=6) # 해당 월드에 beeper를 둘 곳이 6개밖에 없으니까
hubo.set_trace("blue")
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()