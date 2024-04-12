from cs1robots import *

load_world("worlds/trash1.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def move_and_pick():
    while not hubo.on_beeper():
        hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()


def go_back():
    for _ in range(2):
        hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()


def drop_all_beeper():
    while hubo.carries_beepers():
        hubo.drop_beeper()


if __name__ == "__main__":
    while hubo.front_is_clear():
        move_and_pick()

    go_back()
    turn_right()
    hubo.move()

    drop_all_beeper()

    go_back()
    hubo.turn_left()
