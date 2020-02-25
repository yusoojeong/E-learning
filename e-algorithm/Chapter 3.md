## Chapter 3. 알고리즘 평가법

### - 평가의 두 기준 : 시간과 공간

- 시간(★)
- 공간 : 컴퓨터의 저장 공간(메모리)

### - 시간 복잡도 (Time Complexity)

> **데이터**가 많아질수록 **걸리는 시간**이 얼마나 **급격히 증가**하는가
>
> 시간 복잡도가 작을수록 빠른 알고리즘

### - 관련 수학 개념

---

- 거듭제곱 (Exponentiation)

  > 2^3 = 2 x 2 x 2 = 8
  >
  > 2^2 = 2 x 2  = 4
  >
  > 2^1 = 2
  >
  > 2^0 = 1
  >
  > 2^-1 = 1/2

- 로그 (Logarithms)

  > 거듭제곱의 반대 개념
  >
  > ![로그](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FTTClD%2FbtqCcVXrC41%2FXskwFkzGEfxsPKbxbr3OTK%2Fimg.png)
  >
  > b를 a로 몇 번 나누어야 1이 되는가?
  >
  > 아래가 2일 경우 lg16 = 4 같이 쓰기도 함

- 1부터 n까지의 합

  > `(n * (n + 1)) / 2`

---

### - 점근 표기법 (Big-O)

![점근표기법](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fqe5md%2FbtqCjSxkM4a%2FNTS9SHllX9UnkbClvk5xHK%2Fimg.png)

- n이 엄청 크다고 가정

- 절대적 시간이 아닌 **성장성**

- 탐색 알고리즘 평가

  > 선형 탐색 : `O(n)`
  >
  > 이진 탐색 : `O(lg n)`

- 점근 표기법에서 `n`은 인풋크기를 나타내기 위한 문자

### - 주요 시간 복잡도

- *인풋 크기와 상관없이 실행되는 코드*만 `O(1)`. 즉, 인풋 크기가 소요시간에 영향 X

  > 인덱싱 / .append / len() / 값 찾기 / 값 넣기·덮어쓰기·삭제
  >
  > 반복문이 없으면 대체로 `O(1)`

- `O(n)`

  > .reverse() / in / .insert() / del / max·min
  >
  > 반복문이 있고, 반복 횟수가 인풋 크기에 비례 시 `O(n)`

- 그 외

  > .sort() `O(n lg n)` / lst[a:b] `O(b-a)`

- `O(n^2)` : 반복문 안에 반복문

- `O(n^3)` : 반복문 3중첩

- `O(lg n)` : 2배씩 곱하기 or 나누기

- `O(n lg n)` : `O(n)`과 `O(lg n)`이 중첩된 것

### - 공간 복잡도

> 인풋 크기에 비례해서 알고리즘이 사용하는 메모리 공간
>
> 점근 표기법 표현. 즉, Big-O 표기법 사용







