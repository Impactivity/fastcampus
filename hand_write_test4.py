# 문제,
# 숫자 배열이 주어지는데, 배열의 길이의 반 보다도 큰 빈도수를 가지는 숫자를 출력하라.
# 만일 없다면 -1 리턴한다.

import sys
read = sys.stdin.readline
input_array = list(map(int,read().split()))
def number_cnt(arr):
    length = len(arr) // 2
    if length == 0:
        return -1

    answer = []
    num_cnt = {}

    # 딕셔너리 형태로 해당 숫자를 카운트한다.
    for num in arr:
        if num in num_cnt:
            num_cnt[num] += 1
            if num_cnt[num] > length:
                return num
        else:
            num_cnt[num] = 1

    return -1

print(number_cnt(input_array))
