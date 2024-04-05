# task 5 Harvest again

from cs1robots import *

load_world('worlds/harvest2.wld')
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)


def turn_right ():
    for _ in range(3):
        hubo.turn_left()


# 일단 (6, 2)까지 직접 이동.
for _ in range(5):
    hubo.move()
hubo.turn_left()
hubo.move()
hubo.pick_beeper()

# 알고리즘 1 : 대각선으로 지그재그
# 알고리즘 2 : 빙글빙글 - 시계방향


# 대각선 왼쪽 위 이동
def left_up():
    """
    위를 바라보고 있을 때 대각선 왼쪽 위로 이동하는 함수
    :return: None
    """
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.pick_beeper()


# 대각선 오른쪽 위 이동
def right_up():
    """
    위를 바라보고 있을 때, 대각선 오른쪽 위로 이동하는 함수
    :return: None
    """
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.pick_beeper()


# 대각선 오른쪽 아래 이동
def right_down():
    """
    오른쪽을 바라보고 있을 때, 오른쪽 아래로 이동하는 함수
    :return: None
    """
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.pick_beeper()


# 대각선 왼쪽 아래 이동
def left_down():
    """
    아래를 바라보고 있을 때, 대각선 왼쪽 아래로 이동하는 함수
    :return: None
    """
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.pick_beeper()

# 빙글빙글 구현 방법
# 껍질을 하나씩 돌아가는 방식


# 값을 주면 껍질 수만큼 해결.
def one_around(length):
    for _ in range(length - 1):
        left_up()
    for _ in range(length - 1):
        right_up()
    turn_right()
    for _ in range(length - 1):
        right_down()
    turn_right()
    for _ in range(length - 2):
        left_down()


def move_to_bottom():
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.pick_beeper()


# 이 부분만 사용자 입력으로 바꾸면 다양한 상황에 대응할 수 있다.
square_side_length = 6

if __name__ == '__main__':
    while square_side_length > 0:
        one_around(square_side_length)
        if square_side_length <= 2:
            break
        move_to_bottom()
        square_side_length -= 2
