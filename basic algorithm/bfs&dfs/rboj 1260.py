n,m,v = map(int,input().split())
A = [[] for _ in range(n+1)]
for _  in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(1,n+1):
    A[i].sort()

def dfs(v):
    dfs_route.append(v)
    vis[v] = True
    for i in A[v]:
        if not vis[i]:
            dfs(i)

dfs_route = []
vis = [False]*(n+1)      
dfs(v)

from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    vis[v] = True
    
    while q:
        now = q.popleft()
        bfs_route.append(now)
        for i in A[now]:
            if not vis[i]:
                vis[i] = True
                q.append(i)

bfs_route = []
vis = [False]*(n+1)
bfs(v)

print(' '.join(map(str,dfs_route)))
print(' '.join(map(str,bfs_route)))