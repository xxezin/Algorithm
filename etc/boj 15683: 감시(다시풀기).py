import copy
n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)] # 원래 지도
B = copy.deepcopy(A) # 광선이 지나간 후

cctv = [] # cctv 좌표

dx = [1,0,-1,0]
dy = [0,1,0,-1]

bin = 0

# cctv 좌표 저장
for i in range(n):
    for j in range(m):
        if A[i][j] !=0 and A[i][j] !=6:
            cctv.append((i,j))
        elif A[i][j] ==0:
            bin += 1

# 광선이 지나간 거리 저장. 빔빔
def beam(x,y,dir):
    dir = dir%4
    while True:
        x += dx[dir]
        y += dy[dir]
        if x >= m or x < 0 or y >= n or y < 0: # 범위 벗어나거나
            return
        if A[y][x] == 6: # 벽인 경우는 return
            return
        if A[y][x] != 0: # 이미 광선이 지나갔거나 cctv 위치인 경우 continue
            continue
        B[y][x] = 7       

for i in range(4**len(cctv)):
    tmp = i
    for j in range(len(cctv)):
        dir = tmp % 4
        tmp = tmp // 4
        x = cctv[j][1]
        y = cctv[j][0]

        if A[y][x] ==1:
            beam(x,y,dir)
        elif A[y][x] ==2:
            beam(x,y,dir)
            beam(x,y,dir+2)
        elif A[y][x] ==3:
            beam(x,y,dir)
            beam(x,y,dir+1)
        elif A[y][x] ==4:
            beam(x,y,dir)
            beam(x,y,dir+1)
            beam(x,y,dir+2)
        else:
            beam(x,y,dir)
            beam(x,y,dir+1)
            beam(x,y,dir+2)
            beam(x,y,dir+3)
    
    cnt = 0
    for k in range(n):
        for p in range(m):
            if B[k][p] == 0:
                cnt +=1

    bin = min(bin,cnt)
    B = copy.deepcopy(A)

    

print(bin)