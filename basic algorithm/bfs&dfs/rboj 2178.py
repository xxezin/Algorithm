import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    q = deque([(i,j)])
    vis[i][j] = True
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if A[nx][ny] == 1 and not vis[nx][ny]:
                    A[nx][ny] = A[x][y]+1
                    vis[nx][ny] = True
                    q.append((nx,ny))

n,m = map(int,input().split())
A = []
for i in range(n):
    tmp = list(map(int,input().rstrip()))
    A.append(tmp)
vis = [[False]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

bfs(0,0)
print(A[n-1][m-1])