import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
    
def BFS(x):
    q = deque()
    q.append(x)
    
    vis = [-1]*(n+1)
    vis[x] = 0
    while q:
        now = q.popleft()
        for i in A[now]:
            if vis[i] == -1:
                vis[i] = vis[now] + 1
                q.append(i)
    
    bacon = 0
    for i in vis:
        if i != -1:
            bacon += i
    return bacon
    

score = sys.maxsize
lst = []
for i in range(1,n+1):
    tmp = BFS(i)
    if tmp < score:
        score = tmp
        lst = [i]
    elif tmp == score:
        lst.append(i)

if len(lst) == 1:
    print(lst[0])
else:
    lst.sort()
    print(lst[0])
    