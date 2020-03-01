'''
여러 명에서 카드 게임.
각 플레이어는 3장의 카드를 가지고 있음.
한 사람당 카드를 하나씩 뽑아서 모두 곱했을 때 가능한 최대 곱을 찾아라.
Greedy 방식으로 구현
'''

## 내 코드
def max_product(card_lists):
    # 코드를 작성하세요.
    for i in range(len(card_lists)):
        if i == 0:
            ans = max(card_lists[i])
        else:
            ans *= max(card_lists[i])

    return ans

## 해답
def max_product(card_lists):
    # 누적된 곱을 저장하는 변수
    product = 1

    # 반복문을 돌면서 카드 뭉치를 하나씩 본다
    for card_list in card_lists:
        # product에 각 뭉치의 최댓값을 곱해 준다
        product *= max(card_list)

    return product


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))