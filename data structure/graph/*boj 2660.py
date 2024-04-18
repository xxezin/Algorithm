from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n+1)]
q = deque()

while True: # 인접 리스트 생성
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    A[a].append(b)
    A[b].append(a)

# BFS 정의
def BFS(v):
    vis = [-1]*(n+1)
    vis[v] = 0
    q.append(v)
    while q:
        now = q.popleft()
        for i in A[now]:
            if vis[i] == -1:
                vis[i] = vis[now] + 1
                q.append(i)

    return max(vis)
            

chairman = []
score = 50
for i in range(1,n+1):
    tmp = BFS(i)
    if tmp < score:
        score = tmp
        chairman = [i]
    elif tmp == score:
        chairman.append(i)

print(score, len(chairman))
print(*chairman)