def consecutive_sum(start, end):
    # 코드를 작성하세요
    if start == end:
        return start
    else:
        N = (start + end) // 2
        return consecutive_sum(start, N) + consecutive_sum(N+1, end)
        
# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))