# task 4 harvest

from cs1robots import *

load_world("worlds/harvest1.wld")
hubo = Robot(beepers=1)
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def move_pick():
    hubo.move()
    hubo.pick_beeper()


def one_zigzag():
    for _ in range(6):
        move_pick()

    hubo.turn_left()
    move_pick()
    hubo.turn_left()

    for _ in range(5):
        move_pick()

    hubo.move()
    turn_right()


if __name__ == "__main__":
    for _ in range(3):
        one_zigzag()
        hubo.move()
        turn_right()

# 동작 낭비가 좀 있음...
# 과제는 task 5 짜기
# 지그재그는 식상하니까 빙글빙글 돌도록 코딩해보자.
