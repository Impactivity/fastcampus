# 다시 봐야할 문제 !!
# 다시 이해해야함
# DP문제
import sys

read = sys.stdin.readline

N,r,c = map(int,read().split())


# r,c번째 번호를 리턴해주는 함수
def Z(sz ,x ,y):
    if sz == 1 :
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i + 1) and y < sz * (j+1):
                print(sz, x-sz*i, y-sz*j)
                return (i*2+j) * sz*sz + Z(sz, x-sz*i, y-sz*j )
    return

print( Z(N**2, r,c) )
