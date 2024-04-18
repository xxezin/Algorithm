from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
hap = 0
high = 0

for i in range(N):
    hap += sum(A[i])
    high = max(high,max(A[i]))
mean = hap//(N**2)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j,k):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x,y = q.popleft()
        for z in range(4):
            nx = x+dx[z]
            ny = y+dy[z]

            if 0<=nx<N and 0<=ny<N:
                if A[nx][ny]> k and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))

cnt = 0
for i in range(mean-1,high):
    visited = [[False]*N for _ in range(N)]
    ans = 0
    for j in range(N):
        for k in range(N):
            if A[j][k] > i and not visited[j][k]:
                BFS(j,k,i)
                ans +=1
    cnt = max(cnt,ans)

print(cnt)



