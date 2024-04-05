# task 3. Newspaper delivery

from cs1robots import *

load_world("worlds/newspaper.wld")
hubo = Robot(beepers=1)
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def one_step():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()


if __name__ == "__main__":
    for _ in range(4):
        one_step()

    hubo.move()
    hubo.drop_beeper()
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()

    for _ in range(4):
        one_step()