from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n,m,g,r = map(int,input().split())
A = [] # 0: 호수, 1: 배양액 못뿌림, 2: 배양액 뿌릴수 있음
spread = []
for i in range(n):
    A.append(list(map(int,input().split())))
    for j in range(m):
        if A[i][j] == 2:
            spread.append((i,j))
            
ans = 0
select = [0]*(g+r)

INF = sys.maxsize   
dx = [1,0,-1,0]
dy = [0,1,0,-1]


# 꽃을 피우자
def BFS(pos,select):
    vis = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(g+r): # 배양액 사용
        x,y = pos[i]
        color = select[i]
        vis[x][y] = color # 배양액 퍼지는거 표시
        q.append([x,y,color])
    flower = 0
    while q:
        x,y,c = q.popleft()
        if vis[x][y] == INF:
            continue
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if vis[nx][ny] != INF and A[nx][ny] != 0:
                    if vis[nx][ny] == 0:
                        if c < 0:
                            vis[nx][ny] = c-1
                            q.append([nx,ny,c-1])
                        else:
                            vis[nx][ny] = c+1
                            q.append([nx,ny,c+1])
                    else:
                        if abs(vis[nx][ny]) == abs(c)+1: # 꽃이 필 조건
                            if (vis[nx][ny] < 0 and c > 0) or (vis[nx][ny] > 0 and c < 0):
                                flower += 1
                                vis[nx][ny] = INF # 꽃이 핌
    return flower

# 색
def DFS(L,pos,cnt):
    global ans
    if L == g+r:
        ans = max(ans,BFS(pos,select))
        return
    else:
        if cnt[0] > 0: # green
            cnt[0] -= 1
            select[L] = 1
            DFS(L+1,pos,cnt)
            cnt[0] += 1
            
        if cnt[1] > 0: # red
            cnt[1] -= 1
            select[L] = -1
            DFS(L+1,pos,cnt)
            cnt[1] += 1

for pos in combinations(spread,g+r):
    DFS(0,pos,[g,r])
print(ans)