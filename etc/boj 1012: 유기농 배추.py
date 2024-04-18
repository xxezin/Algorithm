from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx>=0 and ny>=0 and nx<M and ny<N:
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*51 for _ in range(51)]
    visited = [[False]*51 for _ in range(51)]

    for _ in range(K):
        i,j = map(int,input().split())
        graph[i][j] = 1


    count = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                BFS(i,j)
                count +=1
    
    print(count)
