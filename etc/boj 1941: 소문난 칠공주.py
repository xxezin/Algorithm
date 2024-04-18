from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

A = [list(map(str,input())) for _ in range(5)]
pos = [] # 좌표
for i in range(5):
    for j in range(5):
        pos.append([i,j])

ans = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for com in combinations(pos,7):
    visited = [[False]*5 for _ in range(5)]
    cnt_S, cnt_Y = 0,0
    cnt = 1
    for x,y in com:
        if A[x][y] == 'S':
            cnt_S +=1
        else:
            cnt_Y +=1
    
    if cnt_S < 4:
        continue

    q = deque()
    q.append((com[0][0],com[0][1]))
    visited[com[0][0]][com[0][1]] = True

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if [nx,ny] in com:
                    q.append((nx,ny))
                    cnt+=1
    if cnt==7:
        ans+=1

print(ans)