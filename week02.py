import random

n_random = random.randrange(1, 100)
win = False

for i in range(7):
    print(f"{7 - i} 번의 기회가 남았습니다. 숫자 입력: ", end = "")
    answer = int(input(""))

    if n_random == answer:
        win = True
        break
    elif n_random > answer:
        print("입력하신 수는 정답보다 작은 수 입니다.")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다.")

if win:
    print("정답입니다!")
else:
    print("정답을 맞추지 못하였습니다!")
