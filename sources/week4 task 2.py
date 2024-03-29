# task 2. Hurdle

from cs1robots import *

load_world("worlds/hurdles1.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


# 한 번 넘는 것만 만들면 된다
# 왜냐하면 하나의 기능만 한 함수가 담당해야 하기 때문
def one_hurdle():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


if __name__ == "__main__":
    for _ in range(4):
        one_hurdle()
    hubo.move()
    hubo.pick_beeper()
