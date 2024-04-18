from collections import deque


F,S,G,U,D = map(int,input().split())
visited = [False]*F # 전체 층만큼 1차원 방문리스트
dist = [0]*F

q = deque()
dx = [U,-D]

def BFS(i):
    q.append(i)
    visited[i] = True
    while q:
        x = q.popleft()
        for k in range(2):
            nx = x+dx[k]
            if x == G-1:
                return dist[x]
            elif 0<=nx<F and not visited[nx]:
                visited[nx] = True
                dist[nx] = dist[x]+1
                q.append(nx)

    

# 강호의 처음 위치에서 BFS 실행
ans = BFS(S-1)
if ans == None:
    print("use the stairs")
else:
    print(ans)