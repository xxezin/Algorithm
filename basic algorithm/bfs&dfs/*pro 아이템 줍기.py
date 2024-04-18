from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    A = [[-1]*(102) for _ in range(102)]
    vis = [[False]*(102) for _ in range(102)]
    
    for rect in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, rect)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    A[i][j] = 0 # 테두리가 아닌 사각형 안
                elif A[i][j] != 0:
                    A[i][j] = 1 # 테두리
                    
    q = deque([(characterX*2,characterY*2)])
    vis[characterX*2][characterY*2] = True
    while q:
        x,y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = A[x][y]//2
            break
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if A[nx][ny] == 1 and not vis[nx][ny]: # 테두리고, 아직 방문 전이면
                vis[nx][ny] = True
                q.append((nx,ny))
                A[nx][ny] = A[x][y]+1
                
    return answer