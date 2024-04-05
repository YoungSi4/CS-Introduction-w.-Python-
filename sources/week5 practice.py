from cs1robots import *

# load_world("worlds/beepers2.wld")
load_world("worlds/amazing1.wld")
hubo = Robot(beepers=100)
hubo.set_trace("green")
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()

# 새로운 기능! hubo.on_beeper()
# beeper 위에 있으면 true 아니면 false


# 이젠 beeper가 없어도 오류가 나지 않아요
# 대신 휴보의 연비가 나빠졌네요...
def move_and_pick():
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()


# beeper를 떨어트리는 건 없을 때도 할 수 있지만 (beeper가 겹쳐짐)
# 일단 없을 때 떨어트리는 함수를 만들어보자
def move_and_drop():
    hubo.move()
    if not hubo.on_beeper():
        hubo.drop_beeper()


def move_or_turn():
    if hubo.front_is_clear():
        dance()
        hubo.move()
    else:
        hubo.turn_left()
    hubo.drop_beeper()


def dance():
    for _ in range(4):
        hubo.turn_left()


if __name__ == "__main__":
    for _ in range(18):
        # move_and_pick()
        # move_and_drop()
        move_or_turn()


## 추가 기능! hubo.front/left/right_is_clear() 벽이 있는지 없는지 알려주는 함수

