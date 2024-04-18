from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
A = [[] for _  in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
    
# 숫자가 작은 것부터 방문하라고 했으니
for i in range(n+1):
    A[i].sort()

def DFS(x): # 재귀로 구현
    vis[x] = True
    print(x,end=' ')
    for i in A[x]:
        if not vis[i]:
            DFS(i)
            
def BFS(x): # 큐로 구현
    q = deque()
    q.append(x)
    vis[x] = True
    while q:
        now = q.popleft()
        print(now,end=' ')
        for i in A[now]:
            if not vis[i]:
                vis[i] = True
                q.append(i)
                
vis = [False]*(n+1)
DFS(v)
print()
vis = [False]*(n+1)
BFS(v)