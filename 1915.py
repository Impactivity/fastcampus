import sys
read = sys.stdin.readline
N,M = map(int,read().split())

A = [ [0 for _ in range(M+1)] for _ in range(N+1)]

# part 4 36번 참
# DP[i][j] = i,j 까지 왔을 때, 가장 큰 정사각형의 한 변의 길이
# A[i][j]가 1인 경우 정사각형 판별,
# 0 1 1     0 0 0
# 1 1 1     0 1 2
# 1 1 ?     0 2 1

# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1] , DP[i][j-1]) + 1

DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for idx, j in enumerate(list(map(int, list(read().rstrip())))):
        A[i+1][idx+1] = j

mx = 0

for i in range(N+1):
    for j in range(M+1):
        if A[i][j] :
            DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - 1], DP[i][j - 1]) + 1
            mx = max(DP[i][j] , mx)


print(mx ** 2 )
