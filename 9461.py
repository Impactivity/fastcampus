import sys

read = sys.stdin.readline

DP = [0] * 101

DP[1] = 1
DP[2] = 1
DP[3] = 1

for i in range(4,101):
    DP[i] = DP[i-2] + DP[i-3]


T = int(read())
for i in range(T):
    N = int(read())
    print(DP[N])