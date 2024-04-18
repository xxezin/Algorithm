# bfs 같음
from collections import deque
def bfs(i,j,maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q = deque()
    q.append((i,j))
    vis[i][j] = True
    cnt = int(maps[i][j])
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny] != "X" and not vis[nx][ny]:
                    vis[nx][ny] = True
                    cnt += int(maps[nx][ny])
                    q.append((nx,ny))
    
    return cnt
    

def solution(maps):
    global vis
    answer = []
    vis = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not vis[i][j]:
                answer.append(bfs(i,j,maps))
    
    if answer == []:
        return [-1]
    else:
        return answer
    
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))