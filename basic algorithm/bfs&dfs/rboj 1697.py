from collections import deque
n,k = map(int,input().split())

q = deque([(n)])
M = 10**5
dist = [0]*(M+1)
while q:
    now = q.popleft()
    if now == k:
        print(dist[now])
        break
    
    for nx in (now+1,now-1,now*2):
        if 0<=nx<=M and dist[nx] == 0:
            dist[nx] = dist[now]+1
            q.append((nx))

