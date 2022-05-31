import sys
read = sys.stdin.readline

n,m = map(int,read().split())

mem_list = {} #멤버들의 속한 팀 정보. 이름 : 소속
team_list = {} #소속 : [이름1,이름2 ....]

for i in range(n):
    team_name,member_len  = read().rstrip(), int(read())

    team_list[team_name] = []
    for j in range(member_len):
        name = read().rstrip()
        team_list[team_name].append(name)
        mem_list[name] = team_name

# 0일경우 해당팀에 속한 멤버들의 이름을 사전순으로 출력
# 1일경우 해당 멤버가 속한 팀의 이름 출력
for k in range(m):
    name = read().rstrip()
    _type = int(read())

    if _type:
        print(mem_list[name])
    else:
        for mem in sorted(team_list[name]):
            print(mem)

