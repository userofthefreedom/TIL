T=int(input())
for i in range(1,T+1):
    row_num, range_num=map(int,input().split())
    fly_base = []
    kill_max = []
    for j in range(row_num):
        fly_base.append(list(map(int,input().split())))
    for r in range(row_num - range_num + 1):
        kill_num = 0


#what to