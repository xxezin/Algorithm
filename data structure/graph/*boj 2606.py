from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    cnt = 0
    q = deque([v])
    vis[v] = True
    
    while q:
        now = q.popleft()
        vis[now] = True
        for i in adj[now]:
            if not vis[i]:
                q.append(i)
                
    return cnt


V = int(input())
N = int(input())
adj = [[] for _ in range(V+1)]
vis = [False]*(V+1)

for _ in range(N):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
    

print(bfs(1)-1)
