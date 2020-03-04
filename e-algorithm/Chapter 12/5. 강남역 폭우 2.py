'''
강남역에 엄청난 폭우가 쏟아졌을 때 건물과 건물 사이 빗물이 담길 수 있는 양을 계산

예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다.
이 경우 0, 3, 3, 1, 3, 0 만큼 빗물이 담길 수 있기 때문에 10이 리턴됩니다.
'''

## 내 코드
def trapping_rain(buildings):
    # 코드를 작성하세요

    left_list = []
    right_list = []
    N = len(buildings)

    for i in range(N):
        if i == 0:
            left_list.append(buildings[0])
        else:
            left_list.append(max(left_list[i - 1], buildings[i - 1]))
    for j in range(N - 1, -1, -1):
        if j == (N - 1):
            right_list.append(0)
        else:
            right_list.insert(0, max(right_list[0], buildings[j + 1]))
    ans = 0
    for k in range(N):
        ans += max(0, min(left_list[k], right_list[k]) - buildings[k])

    return ans

## Brute Force 방식
# def trapping_rain(buildings):
#     # 총 담기는 빗물의 양을 변수에 저장
#     total_height = 0
#
#     # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
#     # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
#     for i in range(1, len(buildings) - 1):
#         # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
#         max_left = max(buildings[:i])
#         max_right = max(buildings[i + 1:])
#
#         # 현재 인덱스에 빗물이 담길 수 있는 높이
#         upper_bound = min(max_left, max_right)
#
#         # 현재 인덱스에 담기는 빗물의 양을 계산
#         # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
#         total_height += max(0, upper_bound - buildings[i])
#
#     return total_height

## 해답
def trapping_rain(buildings):
    total_height = 0  # 총 갇히는 비의 양을 담을 변수
    n = len(buildings)

    # 각각 왼쪽 오른쪽 최대값 리스트 정의
    left_list = [0] * n
    right_list = [0] * n

    # buildings 리스트 각 인덱스 별로 왼쪽으로의 최댓값을 저장한다
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i])

    # buildings 리스트 각 인덱스 별로 오른쪽으로의 최댓값을 저장한다
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])

    # 저장한 값들을 이용해서 총 갇히는 비의 양을 계산한다
    for i in range(n):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(right_list[i], left_list[i])

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))