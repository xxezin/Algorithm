from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

q = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    q.append((i,j))
    visited[i][j]=True
    A[i][j]+=1
    num = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if A[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    A[nx][ny] = A[x][y]+1
                    q.append((nx,ny))
                    num +=1
    return num

cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if A[i][j]==1 and visited[i][j]==False:
            ans.append(BFS(i,j))
            cnt +=1

ans.sort()
print(cnt)
for i in range(cnt):
    print(ans[i],end='\n')