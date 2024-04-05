# 기본적인 코드는 같이 진행
# 과제: 문제를 제시하고 직접 풀이과정을 설명해보는 식으로 진행
# 과제 발표 점수가 있음... 열심히 해봅시다.

# cs1robots 가이드 문서가 있음. 궁금하면 뭐가 있는지 봐보자.
from cs1robots import * # cs1robots 라이브러리의 모든 기능(*)을 불러옴

# create_world()
# hubo = Robot(beepers=10) #Robot()이라는 클래스에서 휴보라는 객체를 생성
# # beepers는 동전임. 나중에 떨어트리고 줍고 한다
# hubo.set_trace("blue") # 지나가는 길의 색상을 정해줌
# hubo.set_pause(0.3) # 휴보의 움직이는 시간을 정해줌
#
# hubo.drop_beeper()
# hubo.move()
# hubo.turn_left()
# hubo.move()
# hubo.drop_beeper() # 보유한 동전이 없으면 에러 발생
# hubo.pick_beeper() # 동전 위에 있지 않으면 에러가 발생함
# hubo.pick_beeper() # 에러 발생
# # 이게 전부.


# 동전을 줍고 돌아오는 맵
# 여러 월드맵이 있고, 시험도 이 중에서 나올 예정
load_world('../worlds/hurdles1.wld')
hubo = Robot()
hubo.set_trace('blue')

# 우회전 함수는 기본적으로 선언하는 편임
def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo.move()
hubo.turn_left()
hubo.move()
turn_right()


# 반복문으로 처리하면 편하겠죠?

