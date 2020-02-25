## 내 풀이
# n의 각 자릿수의 합을 리턴
def sum_digits(n, sum=0):
    # 코드를 작성하세요.
    k = n % 10
    n = n // 10
    sum += k
    if n == 0:
        return sum
    else:
        return sum_digits(n, sum)
    
## 해답
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))