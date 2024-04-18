from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
vis = [False]*(n+1)
cnt = 0

for _ in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
    
q = deque()
q.append(1)
for i in A[1]: # 상근이의 직접적인 친구들을 큐에 넣어둠
    q.append(i)
while q: # 상근이의 친구와 친구의 친구를 세본다
    now = q.popleft()
    vis[now] = True
    for i in A[now]:
        if not vis[i]:
            cnt += 1
            vis[i] = True

print(cnt)