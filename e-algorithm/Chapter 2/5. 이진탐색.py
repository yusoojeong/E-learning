def binary_search(element, some_list):
    # 코드를 작성하세요.
    st = 0
    end = len(some_list)
    while st <= end:
        N = (st + end) // 2
        if some_list[N] == element:
            return N
        elif some_list[N] > element:
            end = N - 1
        else:
            st = N + 1
        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))