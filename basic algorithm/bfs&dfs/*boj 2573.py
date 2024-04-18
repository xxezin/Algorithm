import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque([(x,y)])
    vis[x][y] = True
    melt_list = []
    
    while q:
        melt = 0
        now = q.popleft()
        for k in range(4):
            nx = now[0]+dx[k]
            ny = now[1]+dy[k]
        
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0: # 호수일때
                    melt += 1
                else: # 호수가 아닌 빙산일때
                    if not vis[nx][ny]:
                        vis[nx][ny] = True
                        q.append((nx,ny))
        
        if melt > 0:
            melt_list.append((now[0],now[1],melt))

    for x,y,melt in melt_list:
        graph[x][y] = max(0,graph[x][y]-melt) # 그냥 뺐더니 음수로 갈 때가 있음. 조심!
    
    return 1
            

n,m = map(int,input().split())
graph, ice = [],[] # 그래프와 빙산 위치 리스트
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
    
    for j in range(m):
        if tmp[j] != 0:
            ice.append((i,j))
    
year = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while ice:
    vis = [[False]*m for _ in range(n)]
    cnt = 0 # 덩어리 갯수
    melted = []
    
    for i,j in ice:
        if graph[i][j] != 0 and not vis[i][j]:
            cnt += bfs(i,j)
        if graph[i][j] == 0:
            melted.append((i,j))
    if cnt > 1:
        print(year)
        break
    
    ice = sorted(list(set(ice)-set(melted)))
    year += 1
    
else:
    print(0)