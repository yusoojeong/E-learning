## Chapter 8. Dynamic Programming

> 한 번 계산한 결과를 **재활용 하는 방식**

- 조건

  1. 최적 부분 구조

  2. 중복되는 부분 문제

     → Dynamic Programming으로 문제 해결

- 구현 방법

  1. Memoization
  2. Tabulation



### - 최적 부분 구조 (Optimal Substructure)

> *부분 문제*들의 **최적의 답**을 이용해 *기존 문제*의 **최적의 답**을 구할 수 있다는 것

### - 중복되는 부분 문제 (Overlapping Subproblem)

> 피보나치 같은 경우에 같은 부분을 여러차례 계산한다.



### - Memoization

> cache : 다시 쓸 값을 저장해 놓는 공간



