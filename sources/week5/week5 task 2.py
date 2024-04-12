# 분기를 잘 고려하여 if문의 사용을 최소화 할 것!

# 가위 바위 보
# 3 Pi 2 = 9

player1 = "보"
player2 = "보"

if player1 == player2:
    print("draw")
elif (player1 == "바위" and player2 == "가위") or (player1 == "가위" and player2 == "보") or (player1 == "보" and player2 == "바위"):
    print("player1")
else:
    print("player2")
