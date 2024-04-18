import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
vis = [False]*(n+1)

for _ in range(m):
	u,v = map(int,input().split())
	adj[u].append(v)
	adj[v].append(u)

def DFS(v):
    vis[v] = True
    for i in adj[v]: # 인접한 것들
        if not vis[i]: # 방문 안했으면 DFS
            DFS(i)

cnt = 0
for i in range(1,n+1):
    if not vis[i]:
        cnt += 1
        DFS(i)
        
print(cnt)