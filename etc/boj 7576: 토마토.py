from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i,j))

while queue:
    x,y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx>=0 and ny>=0 and nx<M and ny<N:
            if graph[nx][ny]==0: # 안익은 토마토들
                graph[nx][ny] = graph[x][y]+1 # 이전 일수 +1
                queue.append((nx,ny))

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans,max(line))

print(ans-1)
