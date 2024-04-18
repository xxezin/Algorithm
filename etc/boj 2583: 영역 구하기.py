from collections import deque
import sys
input = sys.stdin.readline

M,N,K = map(int,input().split())
A = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            A[j][k] = -1 # 못가는 곳 매핑

q = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    q.append((i,j))
    A[i][j] = 1
    width = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<M and 0<=ny<N:
                if not visited[nx][ny] and A[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    A[nx][ny] = A[x][y]+1
                    width+=1

    return width


                
cnt = 0
ans = []
for i in range(M):
    for j in range(N):
        if A[i][j]==0:
            ans.append(BFS(i,j))
            cnt += 1
ans.sort()

print(cnt)
for i in range(cnt):
    print(ans[i], end=' ')