## 해설 보고 품 ㅠ
def sublist_max(profits):
    # 코드를 작성하세요.
    max_sum = max_num = profits[0]
    
    for i in range(1, len(profits)):
        max_num = max(max_num + profits[i], profits[i])
        max_sum = max(max_sum, max_num)
        
    return max_sum

## 해답 O(n)
def sublist_max(profits):
    max_profit_so_far = profits[0] # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0] # 가장 끝 요소를 포함하는 구간의 최대 합
    
    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])
        
        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)
    
    return max_profit_so_far

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))