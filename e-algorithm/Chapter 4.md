## Chapter 4. 재귀함수

### - 재귀 (Recursion)

> 재귀 함수 : 자기 자신을 호출하는 함수

### - 팩토리얼 (Factorial)

> 0! = 1
>
> 1! = 1
>
> 2! = 1 x 2 = 2
>
> 3! = 1 x 2 x 3 = 6

- 재귀적으로 문제를 푼다

  = **같은 형태의 더 작은 문제**(부분 문제)를 풀고 답을 이용해서 기존 문제를 푸는 것

- n! 의 예

  > n = 0, n! = 1 (base case)
  >
  > n > 0, n! = (n-1)! x n (recursive case)

### - 반복문 / 재귀 함수

- 재귀 함수

  > 돌아갈 위치를 기억해 둠 - **Call Stack**
  >
  > Call Stack이 너무 많이 쌓이면 stack overflow

