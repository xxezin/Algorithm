from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

visited = [[False]*N for _ in range(N)]
q = deque()

def BFS(x,y):
    q.append((x,y))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==graph[x][y] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

# 일반
visited = [[0]*N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt1 +=1

# 적록색약
visited = [[0]*N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt2+=1

print('{0} {1}'.format(cnt1,cnt2))