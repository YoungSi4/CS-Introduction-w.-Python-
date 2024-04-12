numbers = [2, 4, 6, 8, 10, 12, 14, 16, 37, 74]
is_prime = 0
# 소수인지 검사할 숫자 목록을 numbers에 담는다
# is_prime은 검사 중에 해당 숫자가 소수일 경우
# 1을 할당하여 밑에서 count를 1 늘려줄 때 사용한다.

prime_num_cnt = 0
composite_num_cnt = 0

# numbers에서 숫자를 하나씩 꺼내온다.
for i in numbers:

    # 2부터 꺼내온 숫자 -1 까지 검사
    for j in range(2, i):
        # 나머지가 없으면 (나누어지면) is_prime에 1을 할당.
        # 나머지가 있다면 소수이므로 0 그대로 유지
        if i % j == 0:
            is_prime = 1
            # 나눠지는 것을 확인했다면 이미 소수가 아니므로
            # 더 탐색하지 않고 즉시 탈출
            break

    # 소수인지 아닌지 위에서 판단한 결과에 따라
    # 알맞는 count를 하나 늘려준다.
    if is_prime == 0:
        prime_num_cnt += 1
    else:
        composite_num_cnt += 1

    # 다시 초기값으로 초기화.
    is_prime = 0

# 출력부
print(f'Prime numbers: {prime_num_cnt}')
print(f'Composite numbers: {composite_num_cnt}')