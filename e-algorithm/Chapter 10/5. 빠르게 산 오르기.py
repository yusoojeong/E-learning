'''
등산 중 탈수 방지 위해 1km 당 1L 물 필수
최대한 적은 약수터 들르기
약수터 위치와 물통 용량을 받아와서 약수터 위치 리스트를 리턴
'''

## 내 코드
def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    start_spot = 0
    spots = []
    while True:
        for spot in range(capacity+start_spot, start_spot-1, -1):
            if spot == water_stops[-1]:
                spots.append(spot)
                return spots
            if spot in water_stops:
                start_spot = spot
                spots.append(spot)
                break

## 해답
def select_stops(water_stops, capacity):
    # 약수터 위치 리스트
    stop_list = []

    # 마지막 들른 약수터 위치
    prev_stop = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    # 마지막 약수터는 무조건 간다
    stop_list.append(water_stops[-1])

    return stop_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))