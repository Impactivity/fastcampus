import sys
read = sys.stdin.readline

N,M = map(int,read().split())

A = [list(map(int,read().split())) for _ in range(N)]

# 1,1 부터 i,j까지 부분합
DP = [  [0 for i in range(M+1)] for j in range(N+1) ]


for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + A[i-1][j-1]

for i in range(int(read())):
    i,j,x,y = map(int,read().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1] )