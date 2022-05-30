import sys
read = sys.stdin.readline
n = int(read())
B = list(map(int,read().split()))
A = [0] * n
A[0] = B[0]

for i in range(1,n):
    A[i] = B[i] * (i+1) - sum(A[:i])

for num in A:
    print(num , end = ' ')
