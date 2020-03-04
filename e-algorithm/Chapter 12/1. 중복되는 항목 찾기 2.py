'''
(N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있습니다. 그렇다면 어떤 수는 꼭 한 번은 반복되겠지요.

예를 들어 [1, 3, 4, 2, 5, 4]와 같은 리스트 있을 수도 있고, [1, 1, 1, 6, 2, 2, 3]과 같은 리스트가 있을 수도 있습니다. (몇 개의 수가 여러 번 중복되어 있을 수도 있습니다.)

이러한 리스트에서 반복되는 요소를 찾아내려고 합니다.

중복되는 어떠한 수 ‘하나’만 찾아내도 됩니다. 즉 [1, 1, 1, 6, 2, 2, 3]의 예시에서 1, 2를 모두 리턴하지 않고, 1 또는 2 하나만 리턴하게 하면 됩니다.
'''

## 내 코드
def find_same_number(some_list):
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    # 코드를 쓰세요.
    for some in some_list:
        if some_list.count(some) > 1:
            return some

## 해답
def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list) - 1

    # 반복 요소를 찾으면 리턴한다
    if start == end:
        return start

    # 중간 지점을 구한다
    mid = (start + end) // 2

    # 왼쪽 범위의 숫자를 센다. 오른쪽은 리스트 길이에서 왼쪽 길이를 빼면 되기 때문에 세지 않는다
    left_count = 0

    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1

    # 왼쪽과 오른쪽 범위중 과반 수 이상의 숫자가 있는 범위 내에서 탐색을 다시한다
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)

    return find_same_number(some_list, mid + 1, end)

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
