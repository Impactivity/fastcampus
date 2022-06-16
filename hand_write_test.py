import sys
read = sys.stdin.readline
input_string = read().rstrip()
# 손코딩에서 질문은 입력을 어떻게 받을 것인가 ?
# 입력에 null값으로 들어왔을 경우 어떻게 return 할 것인가 ?
# 손코딩의 역량은 기술적 커뮤니케이션 역량을 보는 것이다.
# 꼼꼼한 프로그래밍 작성 역량


def check(arr):
    if arr is None:
        return False

    if arr == arr[::-1]:
        return True
    else:
        return False

def check2(arr):
    if arr == '' or arr is None:
        return False

    for i in range(0,len(arr)//2):
        if arr[i] != arr[-1-i]:
            return False
    return True

print(check2(input_string))
