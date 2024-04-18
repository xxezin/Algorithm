n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)] # 맵 저장
move = A # CCTV 영역 저장
cctv = [] # CCTV 좌표 저장

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def OOB(a,b): # 범위를 벗어났니?
    if a<0 or a>=n or b<0 or b>=m:
        return True
    
def upd(x,y,dir): # 광선이 지나간 거릐
    dir %= 4
    while 1:
        x += dx[dir]
        y += dy[dir]
        if OOB(x,y) or move[x][y]==6: # 범위를 벗어나거나 벽이면
            return
        if move[x][y] != 0: # 이미 광선이 지나갔으면
            continue
        move[x][y] = 7

mn = 0
for i in range(n):
    for j in range(m):
        if A[i][j] != 0 and A[i][j] != 6: # cctv 좌표 뽑기
            cctv.append((i,j))
        if A[i][j] == 0: # 갈 수 있는 공간
            mn += 1

for tmp in range(0,4**len(cctv)): # cctv 조합
    for i in range(n):
        for j in range(m):
            move[i][j] = A[i][j] # 맵 복사

    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4
        brute //= 4
        x = cctv[i][0]
        y = cctv[i][1]
        if A[x][y]==1:
            upd(x,y,dir)
        elif A[x][y]==2:
            upd(x,y,dir)
            upd(x,y,dir+2)
        elif A[x][y]==3:
            upd(x,y,dir)
            upd(x,y,dir+1)
        elif A[x][y]==4:
            upd(x,y,dir)
            upd(x,y,dir+1)
            upd(x,y,dir+2)
        elif A[x][y]==5:
            upd(x,y,dir)
            upd(x,y,dir+1)
            upd(x,y,dir+2)
            upd(x,y,dir+3)

    sagak = 0
    for k in range(n):
        for p in range(m):
            if move[k][p]==0:
                sagak += 1
    
    mn = min(mn,sagak)

print(mn)