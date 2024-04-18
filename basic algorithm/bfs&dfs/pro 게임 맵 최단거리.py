from collections import deque
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    def bfs(i,j):
        q = deque([(i,j)])
        vis = [[False]*m for _ in range(n)]
        vis[i][j] = True
        
        while q:
            x,y = q.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                    if not vis[nx][ny]:
                        vis[nx][ny] = True
                        q.append((nx,ny))
                        maps[nx][ny] = maps[x][y]+1
                        
    bfs(0,0)
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))