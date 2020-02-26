'''
강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.

그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.

함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.

힌트 : 맨 끝 인덱스에는 물이 담기지 못한다.
힌트2 : 현 인덱스 기준으로 왼쪽과 오른쪽에 더 높은 기둥이 있을 때, 둘 중 낮은 기둥과 현 기둥과의 차이만큼 물이 담길 수 있다.
'''

## 내 코드
def trapping_rain(buildings):
    # 코드를 작성하세요
    ans = 0
    for i in range(1, len(buildings)-1):
        left_height = right_height = buildings[i]
        for j in range(i-1, -1, -1):
            if left_height < buildings[j]:
                left_height = buildings[j]
        for k in range(i+1, len(buildings)):
            if right_height < buildings[k]:
                right_height = buildings[k]
        if left_height < right_height:
            ans += (left_height - buildings[i])
        else:
            ans += (right_height - buildings[i])
            
    return ans 
                           
## 해답
def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height