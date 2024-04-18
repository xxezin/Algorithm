from collections import deque
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수
dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

def BFS():
    q.append(now)
    x,y = now[0], now[1]
    A[x][y] = 1
    while q:
        x,y = q.popleft()
        if x == goal[0] and y == goal[1]:
            return A[x][y]-1
            
        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<I and 0<=ny<I:
                if A[nx][ny]==0:
                    A[nx][ny] = A[x][y]+1
                    q.append([nx,ny])

for _ in range(T):
    I = int(input()) # 체스판 길이
    now = list(map(int,input().split())) # 나이트 현재 위치
    goal = list(map(int,input().split())) # 나이트의 목적 위치

    A = [[0]*I for _ in range(I)] # 그리드
    q = deque() # 큐
    ans = BFS()
    print(ans)
