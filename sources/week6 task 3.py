# 조사할 점수 리스트
scores = [100, 90, 80, 55, 95, 80, 65, 75, 70, 90]
# 점수의 합
sum = 0

# 점수를 sum에 다 더하기
for i in scores:
    sum = sum + 1

# 합을 scores의 길이 (점수의 갯수)로 나눠서 평균 구하기
mean = sum / len(scores)

# variance sum을 0으로 초기화
vsum = 0

# 편차의 제곱 평균을 구하기 위해 일단 vsum에 다 더함
for i in scores:
    vsum = vsum + (i - mean) ** 2

# vsum을 길이 (자료의 갯수)로 나눠서 분산을 구함
variance = vsum / len(scores)

# 평균과 분산 출력
print("Means: ", mean)
print("VarianceL ", variance)