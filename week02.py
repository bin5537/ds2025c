import random

n_random = random.randrange(1, 100)
win = False

for i in range(7):
    if (7 - i) != 1:
        print(f"{7 - i} 번의 기회가 남았습니다. 숫자 입력: ", end="")
    else:
        print("마지막 기회 입니다. 숫자 입력: ", end="")
    answer = int(input(""))

    if n_random == answer:
        win = True
        break
    elif n_random > answer:
        print("입력하신 수는 정답보다 작은 수 입니다.")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다.")

if win:
    print("You Win!")
else:
    print(f"You Lose, The answer is {n_random}")
