from collections import deque
import sys
input = sys.stdin.readline


def bfs(i,j):
    cnt = 1
    q = deque()
    q.append((i,j))
    vis[j][i] = True
    
    while q:
        x,y = q.popleft()
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 > nx or nx >= m or 0 > ny or ny >= n or vis[ny][nx] == True:
                continue
            if adj[ny][nx] == 0:
                continue
            
            q.append((nx,ny))
            vis[ny][nx] = True
            cnt += 1
    
    return cnt

n,m = map(int,input().split())
adj = [list(map(int,input().split())) for _ in range(n)]
vis = [[False]*(m) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer = []
for j in range(n):
    for i in range(m):
        if adj[j][i] == 1 and not vis[j][i]:
            answer.append(bfs(i,j))
     
if answer:       
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)