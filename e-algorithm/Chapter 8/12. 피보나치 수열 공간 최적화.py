def fib_optimized(n):
    # 코드를 작성하세요.
    if n < 2:
        return 1

    previous = 0
    current = 1

    for x in range(2, n + 1):
        previous, current = current, current + previous

    return current

def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다.
    for i in range(1, n):
        current, previous = current + previous, current

    # n번재 피보나치 수를 리턴한다.
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))