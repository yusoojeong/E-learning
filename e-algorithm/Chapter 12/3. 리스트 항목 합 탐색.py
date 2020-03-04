'''
[1, 2, 5, 6, 7, 9, 11] 안에 합이 15가 되는 두 요소의 조합이 있는지 확인하고 싶습니다.
'''
## brute force식 코드
def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    for i in range(len(sorted_list)-1):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == search_sum:
                return True
    return False

## 힌트식 코드
def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    start = 0
    end = len(sorted_list) - 1
    while start < end:
        if sorted_list[start] + sorted_list[end] == search_sum:
            return True

        if sorted_list[start] + sorted_list[end] < search_sum:
            start += 1
        else:
            end -= 1

    return False

## 해답
def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]

        if candidate_sum == search_sum:  # 합이 찾으려는 숫자일 때
            return True

        if candidate_sum < search_sum:  # 합이 찾으려는 숫자보다 작을 때
            low += 1

        else:  # 합이 찾으려는 숫자보다 클 때
            high -= 1

    # 찾는 조합이 없기 때문에 False 리턴
    return False


# 테스트
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))