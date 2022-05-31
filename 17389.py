import sys

read = sys.stdin.readline

N = int(read())
scores = list(map(str, read().rstrip()))
tot_score = 0
bonus = 0
for i in range(1,N+1):
    if scores[i-1] == 'O':
        tot_score ,bonus  = tot_score + i + bonus , bonus + 1
    else:
        bonus = 0

print(tot_score)