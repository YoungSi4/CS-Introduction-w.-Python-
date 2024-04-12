from cs1robots import *

create_world(avenues=10, streets=7)

hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


# 벽까지 쭉 직진하는 함수
# 이전에 반복 횟수를 지정한 것과는 달리
# world의 크기가 바뀌어도 대응할 수 있다
def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()


# move to wall 함수를 포함하여 벽까지 갔다가 다시 돌아오는 함수
def round_trip():
    move_to_wall()
    turn_right()
    if hubo.front_is_clear():
        hubo.move()
        turn_right()
        move_to_wall()
        hubo.turn_left()
        if hubo.front_is_clear():
            hubo.move()
            hubo.turn_left()


# 왼쪽에 벽이 없다면, 왼쪽으로 돌아서
# round trip 함수를 호출
# 벽이 있다면 바로 직진
if hubo.left_is_clear():
    hubo.turn_left()
    while hubo.front_is_clear():
        round_trip()
else:
    move_to_wall()