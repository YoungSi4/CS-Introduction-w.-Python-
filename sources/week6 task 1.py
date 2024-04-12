# 시험 결과가 담긴 리스트
result = [55, 90, 89, 76, 37, 100, 67]
index = 0

# for문으로 result에서 값을 인덱스 0부터
# 하나씩 차례로 꺼내서 i에 담는다
for i in result:

    # 높은 점수부터 판별하여 and나 or을 쓰지 않고도
    # 90점 : A ~ 60점 : D , 그 외 F를 grade에 받아준다.
    if i >= 90:
        grade = 'A'
    elif i > 80:
        grade = 'B'
    elif i >= 70:
        grade = 'C'
    elif i >= 60:
        grade = 'D'
    else:
        grade = 'F'

    index += 1

    # index번 학생은 n점으로 grade를 받았음을 C - style 출력문으로 표시
    print("%d번 학생은 %d점으로 %s입니다." %(index, i, grade))

    # 원래 코드로 하면 출력이 잘 못 되어 index 변수를 새로 만들었습니다.
