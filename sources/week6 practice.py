# 이번 주차는 for while 문

# 새 기능 !
# 앞 오른쪽 왼쪽에 벽이 없는지 파악하는 함수
# hubo.front_is_clear()

from cs1robots import *

create_world()
hubo = Robot(orientation='W', avenue =  7, street = 5)
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()

# 나머지 task들은 코드 해석만 하면 된다
# task 8 은 직접 작성해올 것.
