'''
영훈이는 출근할 때 계단을 통해 사무실로 가는데요.
급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라 갑니다.

한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 방법은 총 몇 가지가 있을까요?
'''
## 내 코드
def staircase(n):
    # 코드를 작성하세요.
    case = [1, 1]

    if n > 1:
        for i in range(2, n + 1):
            case.append(case[i - 1] + case[i - 2])

    return case[n]

## 해답
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))