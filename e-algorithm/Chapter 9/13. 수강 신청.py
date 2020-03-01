'''
이번 학기 수업 리스트를 (시작 교시, 종료 교시)로 주어짐
가장 많은 수업을 들을 수 있는 조합을 찾아주는 함수를 구현

( 힌트 )
# 먼저 시작하는 순으로 정렬
sorted_list = sorted(course_list, key=lambda x: x[0])

# 먼저 끝나는 순으로 정렬
sorted_list = sorted(course_list, key=lambda x: x[1])

# 짧은 순으로 정렬
sorted_list = sorted(course_list, key=lambda x: x[1] - x[0])
'''

## 내 코드
def course_selection(course_list):
    # 코드를 작성하세요.
    course_list.sort()

    before_course = 0
    min_time = 100
    select = []

    while True:
        for course in course_list:
            if course[0] > before_course and course[1] < min_time:
                min_time = course[1]
                element = course
        if not select or select[-1] != element:
            select.append(element)
        elif select[-1] == element:
            break
        before_course = element[1]
        min_time = 100

    return select

## 해답
def course_selection(course_list):
    # 수업을 끝나는 순서로 정렬한다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))