## 입력: 수빈이의 위치와 동생의 위치가 주어짐
## 출력 : 몇초만에 동생을 찾았는지.

# 걷는다면 X-1 또는 X+1
# 순간이동이면 2*X


# 거리를 저장할 dist = 0으로 초기화
from collections import deque

def BFS(N):
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if x == K:
            print(dist[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0 <= nx <= MAX and not dist[nx]: # nx에 아직 다녀가지 않았고, MAX 이내라면
                dist[nx] = dist[x]+1
                queue.append(nx)

MAX = 10**5
dist = [0]*(MAX+1)
N,K = map(int,input().split())

BFS(N)
