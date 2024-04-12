from cs1robots import *

load_world("worlds/hurdles3.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


# 허들을 넘는 함수
def jump_one_hurlde():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


# beeper에 도착할 때까지 이동
while not hubo.on_beeper():
    # 앞에 아무것도 없으면 move. 있으면 허들이므로
    if hubo.front_is_clear():
        hubo.move()
    # 허들을 뛰어넘는 함수를 호출
    else:
        jump_one_hurlde()