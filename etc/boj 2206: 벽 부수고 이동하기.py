from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [list(map(int,input().rstrip())) for _ in range(N)]
move = [[[0,0] for _ in range(M)] for _ in range(N)] # 이동 기록
# flag = [[False]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

q = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    q.append((i,j,0)) # 벽을 부순 횟수를 3번째에 기록해줌
    move[i][j][0] = 1
    while q:
        x,y,cnt = q.popleft()
        if x==N-1 and y==M-1:
            return move[x][y][cnt]
        
        for k in range(4):
            nx =x+dx[k]
            ny =y+dy[k]
            if 0<=nx<N and 0<=ny<M:

                # 벽(=1)인 경우
                if A[nx][ny]==1 and cnt==0:
                    move[nx][ny][1] = move[x][y][0]+1
                    q.append((nx,ny,1))
                
                # 이동 가능하고, 아직 방문하지 않은 경우
                if A[nx][ny]==0 and move[nx][ny][cnt]==0:
                    move[nx][ny][cnt] = move[x][y][cnt]+1
                    q.append((nx,ny,cnt))
    return -1

print(BFS(0,0))

# def BFS(i,j): # 실패
#     q.append((i,j))
#     while q:
#         x,y = q.popleft()
#         visited[x][y] = True
#         for k in range(4):
#             nx = x+dx[k]
#             ny = y+dy[k]
#             if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
#                 if A[nx][ny]==0: # 갈 수 있는 길
#                     q.append((nx,ny))
#                     visited[nx][ny] = True
#                     A[nx][ny] = A[x][y] + 1
#                     flag[nx][ny] = flag[x][y]
#                 elif A[nx][ny]==1 and not flag[x][y]: # 벽인데, 아직 한번도 안뚫은 경우
#                     q.append((nx,ny))
#                     visited[nx][ny] = True
#                     A[nx][ny] = A[x][y]+1
#                     flag[nx][ny] = True
            
#             elif x==N-1 and y==M-1:
#                 return A[x][y]+1


    

