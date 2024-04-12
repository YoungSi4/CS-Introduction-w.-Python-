from cs1robots import *

load_world("worlds/harvest4.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def one_cycle():
    for _ in range(5):
        move_and_pick()
    hubo.turn_left()
    move_and_pick()
    hubo.turn_left()
    for _ in range(5):
        move_and_pick()


if __name__ == "__main__":
    move_and_pick()

    for _ in range(2):
        one_cycle()
        turn_right()
        move_and_pick()
        turn_right()

    one_cycle()