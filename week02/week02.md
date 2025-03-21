## 자료구조 (파이썬을 이용하여 숫자 맞추기 게임, week02)

- 라이브러리
```
import random    // 랜덤한 수를 생성하기 위한 라이브러리 호출
```

- 변수 지정
```
n_random = random.randrange(1, 100)      // 1부터 99 사이의 랜덤 숫자 생성
win = False                              // 사용자 승리 여부 (초기값: False)
```

- 메인 코드
```
// 7번의 기회를 부여하기 위해 반복문 설정
for i in range(7):
    //  남은기회가 1번이 아닌경우
    if (7 - i) != 1:
        // 남은 기회를 출력
        print(f"{7 - i} 번의 기회가 남았습니다. 숫자 입력: ", end="")
    else:
        // 남은기회가 1번인 경우 마지막 기회라는 문구 출력
        print("마지막 기회 입니다. 숫자 입력: ", end="")
    // 사용자에게 값을 입력 받기위해 input (숫자를 입력받기 위해 int 사용)
    answer = int(input(""))

    // 저장된 랜덤값과 사용자가 입력한 값이 동일한 경우 
    if n_random == answer:
        // 사용자 승리여부를 True로 변경 후 반복문을 끝내기 위해 break 
        win = True
        break
    // 저장된 랜덤값이 사용자가 입력한 값보다 크거나 그게 아닌경우 맞는 문구 출
    elif n_random > answer:
        print("입력하신 수는 정답보다 작은 수 입니다.")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다.")
```

- 승리 여부 출력 코드
```
// 사용자가 이긴경우 "You Win!" 문구 출력
if win:
    print("You Win!")
// 사용자가 이기지 못한 경우 문구와 함께 정답(랜덤값)을 출력
else:
    print(f"You Lose, The answer is {n_random}")```
