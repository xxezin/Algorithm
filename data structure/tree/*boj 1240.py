import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,dis = map(int,input().split())
    tree[a].append([b,dis])
    tree[b].append([a,dis])
  
def BFS(start,find):
    q = deque()
    q.append((start,0))
    vis = [False]*(n+1)
    vis[start] = True
    while q:
        now,dis = q.popleft()
        if now == find:
            return dis
        for i in tree[now]:
            if not vis[i[0]]:
                vis[i[0]] = True
                q.append((i[0],dis+i[1]))               
    


for _ in range(m): # 알고 싶은 노드 쌍의 수
    a,b = map(int,input().split())
    print(BFS(a,b))