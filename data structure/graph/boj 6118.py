from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
for _ in range(m): # 인접 리스트 생성
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
vis = [-1]*(n+1)

def BFS(v):
    q = deque()
    q.append(v)
    
    vis[v] = 0
    while q:
        now = q.popleft()
        for i in A[now]:
            if vis[i] == -1:
                vis[i] = vis[now] + 1
                q.append(i)
    return vis # vis 자체를 dist 같이 저장

tmp = BFS(1)
M = max(tmp)
lst = []
cnt = 0
for i in range(len(tmp)):
    if tmp[i] > M:
        lst = [i]
        cnt = 1
        M = tmp[i]
    elif tmp[i] == M:
        lst.append(i)
        cnt += 1

lst.sort()
        
print(f'{lst[0]} {M} {cnt}')