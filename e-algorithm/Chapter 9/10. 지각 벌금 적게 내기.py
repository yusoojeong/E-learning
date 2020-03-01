'''
지각 시 1분마다 벌금 1달러
악보 출력해서 가야함. 주어진 수는 출력해야할 페이지 수
프린트는 1대. 1장을 출력하기 위해서는 1분이 걸림.
최소 벌금 내는 방법을 Greedy로 구현
'''

## 내 코드
def min_fee(pages_to_print):
    # 코드를 작성하세요.
    pages_to_print.sort()
    N = len(pages_to_print)
    ans = 0

    for i in range(N):
        ans += pages_to_print[i] * (N - i)

    return ans

## 해답
def min_fee(pages_to_print):
    # 인풋으로 받은 리스트를 정렬시켜 준다
    sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
