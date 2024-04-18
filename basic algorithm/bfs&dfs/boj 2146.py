import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    global bridge
    vis[i][j] = True
    q = deque([(i,j)])
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            
            
       

n = int(input())
graph = []
land = [] # 대륙의 좌표
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == 1:
            land.append((i,j))
            
vis = [[False]*n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

bridge = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i,j)
 
answer = 101        
for i,j in bridge:
    answer = min(answer,graph[i][j])
    
print(answer-1)