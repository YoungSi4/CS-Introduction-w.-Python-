from cs1robots import *

load_world("worlds/harvest3.wld")

hubo = Robot(beepers=6) # 해당 월드에 beeper를 둘 곳이 6개밖에 없으니까
hubo.set_trace("blue")
hubo.set_pause(0.1)


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def move_and_drop():
    hubo.move()
    if not hubo.on_beeper():
        hubo.drop_beeper()


def one_cycle():
    for _ in range(5):
        move_and_drop()
    hubo.turn_left()
    move_and_drop()
    hubo.turn_left()
    for _ in range(5):
        move_and_drop()


if __name__ == "__main__":
    # 반복 시작점으로 이동
    hubo.move()

    # 2번 반복
    for _ in range(2):
        one_cycle()
        turn_right()
        hubo.move()
        turn_right()

    # 마지막은 반복 시작점으로 이동할 필요가 없음
    # 따라서 함수만 한 번 호출
    one_cycle()
