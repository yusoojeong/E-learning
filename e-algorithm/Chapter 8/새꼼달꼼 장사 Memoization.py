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


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
