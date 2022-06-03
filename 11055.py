import sys
import copy
read = sys.stdin.readline

n = int(read())
A = list(map(int,read().split()))

DP = copy.deepcopy(A)

rev = [ [] for _ in range(n)] # 증가 수열 저장

for i in range(1,n):
    for j in range(i):
        if A[i] > A[j] and DP[i] < A[i] + DP[j]:
            DP[i] = A[i] + DP[j]
            rev[i].append(j)
    rev[i].append(i)

print(max(DP))