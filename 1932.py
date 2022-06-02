import sys
read = sys.stdin.readline

n = int(read())
graph = [[] for _ in range(n)]
DP = [[0] * (n) for _ in range(n)]


for i in range(0,n):
    graph[i] = list(map(int,read().split()))

DP[0][0] = graph[0][0]

for i in range(1,n):
    for j in range(0,len(graph[i])):
        DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + graph[i][j]

print(max(DP[-1]))