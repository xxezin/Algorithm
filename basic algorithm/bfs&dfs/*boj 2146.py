from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
adj = [list(map(int,input().split())) for _ in range(N)]
graph = [[0]*(N) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

## flood fill
# bfs시 시간 초과
# cnt = 0
# for y in range(N):
#     for x in range(N):
#         if adj[y][x] == 1: # 육지면
#             cnt += 1
#             q = deque([[x,y]])
#             while q:
#                 x,y = q.popleft()
#                 graph[y][x] = cnt
#                 adj[y][x] = 0
                
#                 for k in range(4):
#                     nx, ny = x + dx[k], y + dy[k]
#                     # 범위를 넘어가거나 육지가 아니면
#                     if 0 > nx or N <= nx or 0 > ny or N <= ny or adj[ny][nx] != 1:
#                         continue
                        
#                     q.append([nx,ny])
cnt = 0
for y in range(N):
    for x in range(N):
        if adj[y][x] == 1:
            cnt += 1
            stack = [(x,y)]
            while stack:
                x,y = stack.pop()
                graph[y][x] = cnt
                adj[y][x] = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 > nx or N <= nx or 0 > ny or N <= ny or adj[ny][nx] != 1:
                        continue
                    stack.append((nx,ny))

# 육지 좌표 저장
land = defaultdict(list)
for y in range(N):
    for x in range(N):
        if graph[y][x] != 0:
            land[graph[y][x]].append((x,y))

# 최단 경로 찾기
answer = 10001
for key, value in land.items(): # k - 섬 번호, v - 육지 좌표
    vis = [[-1] * N for _ in range(N)]
    
    # 육지 좌표는 0으로
    for x,y in value:
        vis[y][x] = 0
    
    q = deque(value)
    check = False # 현재 섬에서 다른 섬에 닿았는지 확인하는 플래그
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 > nx or N <= nx or 0 > ny or N <= ny:
                continue
            
            # 다른 섬과 만남
            if graph[ny][nx] > 0 and graph[ny][nx] != key:
                answer = min(answer, vis[y][x])
                check = True
                break
            
            # 처음 바다를 만남
            if graph[ny][nx] == 0 and vis[ny][nx] == -1:
                vis[ny][nx] = vis[y][x] + 1
                q.append([nx,ny])
            
            if check:
                break
    
print(answer)