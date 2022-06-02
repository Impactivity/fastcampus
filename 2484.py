import sys
read = sys.stdin.readline

answer = 0
N = int(read())
for _ in range(N):
    dice = sorted(list(map(int,read().split())) , reverse = True)
    if len(set(dice)) == 1:
        answer = max(answer, 50000+dice[0]*5000)
    elif len(set(dice)) == 2:
        if dice[1] == dice[2]:
            answer = max(answer, 10000 + dice[1] * 1000)
        else :
            answer = max(answer, 2000 + dice[1] * 500 + dice[2] * 500)
    elif len(set(dice)) == 3:
        answer = max(answer, 1000 + dice[1]*100)
    elif len(set(dice)) == 4:
        answer = max(answer, dice[0] * 100)
print(answer)
