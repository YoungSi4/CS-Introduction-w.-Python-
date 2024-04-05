# task 1
# input으로 사용자 입력하지 말고 변수를 tuple로 초기화해서 사용할 것
# x값과 y값을 비교해서 조건을 분기해주자

a = (5, -5)
b = (-5, 5)

if a[0] == b[0] and a[1] == b[1]:
    print("same")
elif a[0] == -b[0] and a[1] == b[1]:
    print("Y-axis symmetry")
elif a[0] == b[0] and a[1] == -b[1]:
    print("X-axis symmetry")
elif a[0] == -b[0] and a[1] == -b[1]:
    print("origin symmetry")
else:
    print("nothing")
