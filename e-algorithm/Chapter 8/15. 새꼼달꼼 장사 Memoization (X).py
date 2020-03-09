'''
문제
솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다. 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...

가능한 최대 수익을 리턴시켜 주는 함수 max_profit_memo를 Memoization 방식으로 작성해 보세요. max_profit_memo는 파라미터 세 개를 받습니다.

price_list: 개수별 가격이 정리되어 있는 리스트
count: 판매할 새꼼달꼼 개수
cache: 개수별 최대 수익이 저장되어 있는 사전
예를 들어 price_list가 [0, 100, 400, 800, 900, 1000]이라면,

새꼼달꼼 0개에 0원
새꼼달꼼 1개에 100원
새꼼달꼼 2개에 400원
새꼼달꼼 3개에 800원
새꼼달꼼 4개에 900원
새꼼달꼼 5개에 1000원
이렇게 가격이 책정된 건데요. 만약 솔희가 새꼼달꼼 5개를 판매한다면 최대로 얼마를 벌 수 있을까요?

힌트 1.
재귀 함수를 작성할 때에는 base case와 recursive case에 대해 생각해야 합니다.

Recursive case: 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우
Base case: 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우

힌트 2.
새꼼달꼼 2개를 팔아서 가능한 최대 수익은 어떻게 찾아낼 수 있을까요?

2개를 한 명에게 팔 때의 가격
1개를 팔아서 가능한 최대 수익 + 1개를 팔아서 가능한 최대 수익
위 두 경우를 비교하면 됩니다. 그렇다면 새꼼달꼼 3개를 팔아서 가능한 최대 수익은 어떻게 찾아낼 수 있을까요?

3개를 한 명에게 팔 때의 가격
2개를 팔아서 가능한 최대 수익 + 1개를 팔아서 가능한 최대 수익
위 두 경우를 비교하면 됩니다. 그렇다면 새꼼달꼼 4개를 팔아서 가능한 최대 수익은 어떻게 찾아낼 수 있을까요?

4개를 한 명에게 팔 때의 가격
3개를 팔아서 가능한 최대 수익 + 1개를 팔아서 가능한 최대 수익
2개를 팔아서 가능한 최대 수익 + 2개를 팔아서 가능한 최대 수익
위 세 경우를 비교하면 됩니다. 그렇다면 새꼼달꼼 5개를 팔아서 가능한 최대 수익은 어떻게 찾아낼 수 있을까요?

5개를 한 명에게 팔 때의 가격
4개를 팔아서 가능한 최대 수익 + 1개를 팔아서 가능한 최대 수익
3개를 팔아서 가능한 최대 수익 + 2개를 팔아서 가능한 최대 수익
위 세 경우를 비교하면 됩니다. 그렇다면 새꼼달꼼 6개를 팔아서 가능한 최대 수익은 어떻게 찾아낼 수 있을까요?

6개를 한 명에게 팔 때의 가격
5개를 팔아서 가능한 최대 수익 + 1개를 팔아서 가능한 최대 수익
4개를 팔아서 가능한 최대 수익 + 2개를 팔아서 가능한 최대 수익
3개를 팔아서 가능한 최대 수익 + 3개를 팔아서 가능한 최대 수익
위 네 경우를 비교하면 됩니다. 패턴이 보이시나요?

'''

## 내 코드 // 실패
def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    if count < 4:
        cache[count] = max(price_list[count], max_profit_memo(price_list, count - 1, cache) + cache[1])
    elif count < len(price_list):
        a = max_profit_memo(price_list, count - 1, cache) + cache[1]
        b = max_profit_memo(price_list, count - 2, cache) + cache[2]
        cache[count] = max(price_list[count], a, b)
    else:
        a = max_profit_memo(price_list, count - 1, cache) + cache[1]
        b = max_profit_memo(price_list, count - 2, cache) + cache[2]
        c = max_profit_memo(price_list, count - 3, cache) + cache[3]
        cache[count] = max(a, b, c)
    return cache[count]

## 해답
def max_profit_memo(price_list, count, cache):
    # Base Case: 0개 혹은 1개면 부분 문제로 나눌 필요가 없기 때문에 가격을 바로 리턴한다
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
    # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache)
                 + max_profit_memo(price_list, count - i, cache))

    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit

    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))