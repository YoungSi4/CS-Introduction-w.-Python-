# string으로 처리하라는 게 포인트!

# 고려사항 1. 30분을 뺀다
# 고려사항 2. 30보다 작으면 시간을 1 줄이고 분에 30을 더한다
# 고려사항 3. 만약 시간이 00이라면 시간을 23으로 바꾸고 분에 30을 더한다.


# 너무 비효율적이네요... :(
# 값이 한 자리 숫자가 되었을 때, 0n 식으로 표기해주기 위한 함수
def input_zero(n) -> str:
    """
    한 자리 숫자인 int를 str로 변환하고 앞에 0을 붙임
    :param n: int
    :return: str ( "0" + "n" )
    """
    n = '0' + str(n)
    return n


if __name__ == "__main__":
    # 변수 선언부
    hour, minute = input("time (hh:mm) = ").split(":")
    minute = int(minute)

    # 30분 빼주기
    if minute >= 30:
        minute -= 30

        if minute // 10 == 0:
            minute = input_zero(minute)

    else:
        minute += 30
        if hour == "00":
            hour = "23"
        else:
            hour = int(hour) - 1

            if hour // 10 == 0:
                hour = input_zero(hour)

    print(f"{hour}:{minute}")
