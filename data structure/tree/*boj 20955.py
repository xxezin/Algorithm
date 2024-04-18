import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
tree = [[] for _ in range(n+1)]
vis = [False]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = -1
edge = 0 # 사용하는 간선 갯수
# 전체 간선 갯수 - 사용하는 간선 갯수로 사이클을 만드는 간선을 끊음
for i in range(1,n+1):
    if not vis[i]:
        ans += 1
        vis[i] = True
        q = deque()
        q.append(i)
        
        while q:
            now = q.popleft()
            for nx in tree[now]:
                if not vis[nx]:
                    vis[nx] = True
                    q.append(nx)
                    edge += 1
                    
print(ans + m - edge)
