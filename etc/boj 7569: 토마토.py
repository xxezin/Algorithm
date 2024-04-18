from collections import deque
import sys
input = sys.stdin.readline

M,N,H = list(map(int,input().split())) # 토마토 상자 크기
A = [[[]*M for _ in range(N)] for _ in range(H)]# 토마토 상자
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        A[i][j] = list(map(int,input().split()))

q = deque()
dz = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dx = [0,0,1,0,0,-1]

flag1 = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if A[i][j][k] == 1:
                q.append((i,j,k))
            else:
                flag1 = True

while q:
    z,y,x = q.popleft()
    for m in range(6):
        nz = z + dz[m]
        ny = y + dy[m]
        nx = x + dx[m]
        if 0<=nz<H and 0<=ny<N and 0<=nx<M:
            if A[nz][ny][nx] == 0:
                A[nz][ny][nx]= A[z][y][x]+1
                q.append((nz,ny,nx))
            
flag2 = True
cnt = 0
for i in range(H):
    for j in range(N):
        cnt = max(cnt,max(A[i][j]))
        for k in range(M):
            if A[i][j][k]==0:
                flag2 = False


if flag1:
    if flag2:
        print(cnt-1)
    else:
        print(-1)
else:
    print(0)
