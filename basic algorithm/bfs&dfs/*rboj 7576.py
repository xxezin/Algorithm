# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
A = [] # 초기 밭
q = deque()
for i in range(n):
    tmp = list(map(int,input().split()))
    A.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            q.append((i,j)) # 처음부터 익은 토마토 위치

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if A[nx][ny] == 0:
                A[nx][ny] = A[x][y]+1
                q.append((nx,ny))

ans = 0
for line in A:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans,max(line))
print(ans-1)