import sys
from collections import deque
input = sys.stdin.readline

# 조건 1: 인접한 칸에 좋아하는 학생 수
def like(v):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    tmp = []
    for x in range(n):
        for y in range(n):
            if not A[x][y]:
                l = 0
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<n and 0<=ny<n and A[nx][ny] in L[v]:
                        l += 1
                        
                if tmp == []:
                    tmp.append((l,x,y))
                elif (tmp and tmp[0][0] == l):
                    tmp.append((l,x,y))
                elif (tmp and tmp[0][0] < l):
                    tmp = []
                    tmp.append((l,x,y))
                
    return tmp

# 조건 2: 조건 1을 만족하는 칸이 여러개면, 인접한 칸 중 비어있는 칸이 가장 많은 칸으로
def blank(arr):
    arr = deque(arr)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    tmp = []
    while arr:
        l,x,y = arr.popleft()
        b = 0
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and not A[nx][ny]:
                b += 1
        
        if tmp == []:
            tmp.append((b,x,y))
        elif (tmp and tmp[0][0] == b):
            tmp.append((b,x,y))
        elif (tmp and tmp[0][0] < b):
            tmp = []
            tmp.append((b,x,y))
            
    return tmp

n = int(input())
L = [[] for _ in range(n**2+1)]
A = [[0]*n for _ in range(n)]
seats = [] # 앉는 순서
for _ in range(n**2):
    tmp = list(map(int,input().split()))
    L[tmp[0]] = tmp[1:]
    seats.append(tmp[0])
 
# 조건 3: 1,2 모두 충족하는 칸이 여러개면, 행의 번호가 작은 칸... 그런칸도 여러개면 열의 번호가 가장 작은 칸으로 자리를 정함
for seat in seats:
    tmp1 = like(seat)
    if len(tmp1) > 1: # 조건 1 여러개
        tmp2 = blank(tmp1)
        if len(tmp2) > 1: # 조건 2 여러개
            tmp2.sort(key=lambda x:(x[1],x[2]))
            A[tmp2[0][1]][tmp2[0][2]] = seat
        else: # 조건 2 한개
            A[tmp2[0][1]][tmp2[0][2]] = seat
    
    else: # 조건 1 한개
        A[tmp1[0][1]][tmp1[0][2]] = seat

dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0
for x in range(n):
    for y in range(n):
        good = 0
        stud = A[x][y]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and A[nx][ny] in L[stud]:
                good += 1
        if good == 0 or good == 1:
            answer += 1
        elif good == 2:
            answer += 10
        elif good == 3:
            answer += 100
        elif good == 4:
            answer += 1000
            
print(answer)