import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    area = 1
    vis[i][j] = 1
    q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if A[nx][ny] == 1 and vis[nx][ny] == 0:
                    vis[nx][ny] = vis[x][y]+1
                    q.append((nx,ny))
                    area += 1
    return area

n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
vis = [[0]*m for _ in range(n)]
q = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer = 0
M = 0
for i in range(n):
    for j in range(m):
        if A[i][j] == 1 and vis[i][j] == 0:
            M = max(M,bfs(i,j))
            answer += 1
            
print(answer)
print(M)