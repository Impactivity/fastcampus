import sys
read = sys.stdin.readline

C = [0,0,0]
M = [0,0,0]

for i in range(3):
    C[i], M[i] = map(int,read().split())

for i in range(100):
    #현재 비커의 우유 양
    cur_idx,next_idx = i%3 , (i+1)%3
    M[cur_idx], M[next_idx] = M[cur_idx] -  min(M[cur_idx], C[next_idx]-M[next_idx]) \
        ,M[next_idx] + min(M[cur_idx], C[next_idx] - M[next_idx])
    # M[cur_idx], M[next_idx] = max(M[cur_idx] - (C[next_idx]- M[next_idx]), 0) \
    #     , min(C[next_idx], M[next_idx] + M[cur_idx])
for i in range(3):
    print(M[i])
