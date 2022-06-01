import sys

read = sys.stdin.readline
T = int(read())
answer = []
def add_candy():
    length = len(C)
    for i in range(length):
        if C[i] % 2 != 0: #홀수일때 1개를 더하여서 짝수로
            C[i] += 1

def ditribute():
    length = len(C)
    after = [0] * length
    for i in range(length):
        after[(i+1) % length] = C[i] // 2
        C[i] = C[i] // 2

    for i in range(length):
        C[i] += after[i]

def check():
    length = len(C)
    for i in range(1,length):
        if C[i] != C[i-1]:
            return False
    return True

for _ in range(T):
    #아이들의 수
    N = int(read())
    # 아이들이 초기에 가지고있는 사탕의 갯수
    C = list(map(int,read().split()))
    circle = 0
    # 초기 홀수는 짝수로 만들어준다.
    add_candy()
    is_True = check()
    if is_True == True:
        answer.append(circle)
        continue

    while True:
        ditribute() #분배
        add_candy() #홀수->짝수
        circle+=1 # 순환 + 1
        is_True = check()
        if is_True:
            break

    answer.append(circle)

for num in answer:
    print(num)


