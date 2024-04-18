import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 불이랑 상근이의 BFS를 각각 만들어야할듯
def sang(): # 상근
    while q1:
        x,y = q1.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<H and 0<=ny<W and dist1[nx][ny]==0:
                dist1[nx][ny] = dist1[x][y]+1
                q1.append((nx,ny))
            elif x==0 or x==H-1 or y==0 or y==W-1:
                if (dist1[x][y]>0 and dist1[x][y]<dist2[x][y]) or (dist1[x][y]>0 and dist2[x][y]==0):
                    return dist1[x][y]
    

        
            
def fire(): # 불
    while q2:
        x,y = q2.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<H and 0<=ny<W and dist2[nx][ny]==0:
                dist2[nx][ny] = dist2[x][y]+1
                q2.append((nx,ny))


    

for _ in range(T): # 테스트 케이스 만큼
    W,H = map(int,input().split())
    A = [list(input().rstrip()) for _ in range(H)] # 그림
    
    dist1 = [[-1]*W for _ in range(H)] # 상근
    dist2 = [[-1]*W for _ in range(H)] # 불
    q1 = deque()
    q2 = deque()
    
    for i in range(H):
        for j in range(W):
            if A[i][j] == '@': # 상근이 위치
                dist1[i][j] = 1
                dist2[i][j] = 0
                q1.append((i,j))
            elif A[i][j] == '*': # 불 위치
                dist2[i][j] = 1
                q2.append((i,j))
            elif A[i][j] =='.': # 빈 공간 위치
                dist1[i][j] = 0
                dist2[i][j] = 0
            # 벽은 dist1, dist2에서 모두 -1로 매핑되어 있음

    fire()
    S = sang()
    if S == None:
        print('IMPOSSIBLE')
    else:
        print(S)

