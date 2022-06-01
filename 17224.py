import sys

read = sys.stdin.readline
N,L,K = map(int,read().split()) # 1 <= N <= 100, # 1 <= L <= 50 , 0 <= K <= N

problems = []
for _ in range(N):
    sub1, sub2 = map(int,read().split())
    problems.append([sub1,sub2])

problems.sort(key=lambda k:k[1])
tot_score = 0
for sub1, sub2 in problems:
    if K > 0:
        if sub2 <= L:
            tot_score += 140
            K -= 1
        elif sub1 <= L:
            tot_score += 100
            K -= 1
print(tot_score)

