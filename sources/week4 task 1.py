# taks 1. zigzag

from cs1robots import *

create_world()

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def go_9_blocks():
    for _ in range(9):
        hubo.move()

def one_zigzag():
    hubo.turn_left()
    go_9_blocks()
    turn_right()
    hubo.move()
    turn_right()
    go_9_blocks()

for _ in range(4):
    one_zigzag()
    hubo.turn_left()
    hubo.move()

one_zigzag()

# zigzag만 함수화, 9칸 가는 걸 함수화. 둘을 합치면 코드가 매우 간결해짐.
