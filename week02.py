import random

n_random = random.randrange(1, 100)

for i in range(3):
    answer = int(input("정수 입력: "))

    if n_random == answer:
        print("정답입니다.")
        break
    elif n_random > answer:
        print("입력하신 수는 정답보다 작은 수 입니다.")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다.")
