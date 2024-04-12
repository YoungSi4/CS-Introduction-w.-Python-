from cs1robots import *

create_world()

# 휴보의 최초 상태를 서쪽을 바라보고, (7, 5) 에 둠
hubo = Robot(orientation='W', avenue=7, street=5)
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()


# 휴보가 북쪽을 바라볼 때까지 회전
# 방향이 랜덤일 때, 방향을 정할 기준이 필요하기 때문
while not hubo.facing_north():
    hubo.turn_left()

# x축 y축으로 벽에 닿을 때까지 왼쪽, 아래로 움직이면 되니까
# for로 2번 반복 시킴
for i in range(2):
    hubo.turn_left()
    move_to_wall()

# 동쪽을 바라봄. 휴보를 아무것도 없이 객체로 생성했을 때
# 기본값인 동쪽으로 맞춰주기 위함
hubo.turn_left()