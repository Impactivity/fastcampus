import sys
read = sys.stdin.readline

n = int(read())

DP = [0] * 1001

DP[0] = 1
DP[1] = 1

for i in range(2,n+1):
    DP[i] = (DP[i-1] + DP[i-2]) % 10007

print(DP[n])