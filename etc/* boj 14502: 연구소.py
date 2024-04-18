# 바이러스의 확산을 막기 위해 연구소에 벽을 세우려고 함
# 벽 ... 모든 경우의 수... 조합
# 벽을 세우고 바이러스 퍼지게 한뒤 안전영역의 크기를 잰다.
# 그 중 최대를 구한다.

# 0 : 빈칸, 1: 벽, 2: 바이러스

# 입력 : 지도의 세로 N, 가로 M (3 <= N,M <= 8)
#       지도의 모양
#       2(바이러스)의 개수는 2 ~ 10 사이
#       빈 칸의 개수는 3개 이상
# 출력 : 얻을 수 있는 안전 영역의 최대 크기

# 필요 1 : 모든 경우의 수로 벽을 세워본다.
# 필요 2 : 바이러스를 퍼지게 한다.
# 필요 3 : 안전 영역의 크기를 잰다. 그리고 최댓값을 뱉는다.

## 시도 1 ## 시간 초과 ##
# from collections import deque
# import copy
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# A = [list(map(int,input().split())) for _ in range(n)] # 원래 지도
# B = copy.deepcopy(A) # 바이러스 퍼트린 후를 저장할 지도
# ans = 0

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]


# def bfs():
#     q = deque()
#     B = copy.deepcopy(A)

#     for i in range(n):
#         for j in range(m):
#             if B[i][j]==2:
#                 q.append((i,j))
    
#     while q:
#         x,y = q.popleft()
#         for k in range(4):
#             nx = x+dx[k]
#             ny = y+dy[k]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
            
#             if B[nx][ny]==0:
#                 B[nx][ny]=2
#                 q.append((nx,ny))
    
#     global ans
#     cnt = 0
#     for i in range(n):
#         cnt += B[i].count(0)
    
#     ans = max(ans,cnt)

# def wall(cnt):
#     if cnt == 3:
#         bfs()
#         return
        
#     for i in range(n):
#         for j in range(m):
#             if A[i][j] == 0:
#                 A[i][j] = 1
#                 wall(cnt+1)
#                 A[i][j] = 0

# wall(0)
# print(ans)

## 시도 2 ## 조합을 사용하는 방법
import sys; input = sys.stdin.readline
import copy
from itertools import combinations

def check():
    global answer
    # 새로 세우는 벽 3개에 대한 조합을 얻는다
    for walls in combinations(empty, 3):
        # 기존 맵에 대한 복사
        B = copy.deepcopy(A)

        # 얻은 조합마다 벽을 세움
        for x_w,y_w in walls:
            B[x_w][y_w] =1

        # 바이러스 위치
        virus = [(i,j) for i in range(n) for j in range(m) if B[i][j]==2]

        # 바이러스 전파
        while virus:
            x,y = virus.pop()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<n and 0<=ny<m and B[nx][ny]==0:
                    B[nx][ny]=2
                    virus.append((nx,ny))
        

        # 안전지대 세기
        safe_cnt = 0
        for row in B:
            safe_cnt += row.count(0)
        answer = max(answer,safe_cnt)


n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
empty = [(i,j) for i in range(n) for j in range(m) if A[i][j]==0]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
    
answer = 0
check()   
print(answer)

        
        

