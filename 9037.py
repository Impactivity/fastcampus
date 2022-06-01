import sys

read = sys.stdin.readline
T = int(read())

def add_candy():
    length = len(C)
    for i in range(length):
        if C[i] % 2 != 0: #홀수일때 1개를 더하여서 짝수로
            C[i] += 1

def ditribute():
    length = len(C)
    after = [0] * length # 분배한 갯수 저장하는 리스트
    for i in range(length):
        after[(i+1) % length] = C[i] // 2
        C[i] = C[i] // 2

    for i in range(length):
        C[i] += after[i]

def check(): #모두다 같은 갯수인지 체크
    return len(set(C)) == 1


for _ in range(T):
    # N :아이들의 수 , C : 아이들이 초기에 가지고있는 사탕의 갯수
    N,C = int(read()),list(map(int,read().split()))
    circle = 0
    # 초기 홀수는 짝수로 만들어준다.
    add_candy()
    while not check():
        ditribute() #분배
        add_candy() #홀수->짝수
        circle+=1 # 순환 + 1
    print(circle)


