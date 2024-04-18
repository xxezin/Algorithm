import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
m = int(input())

A = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    A[x].append(y)
    A[y].append(x)
    
for i in range(1,n+1):
    A[i].sort()
    
def bfs(v):
    q = deque()
    q.append(v)
    vis[v] = 1
    
    while q:
        now = q.popleft()
        if now == b:
            return vis[now]-1
        
        for i in A[now]:
            if vis[i] == 0:
                vis[i] = vis[now] + 1
                q.append(i)
    return -1

vis = [0]*(n+1)
print(bfs(a))
