import sys
from collections import deque
input = sys.stdin.readline  

def bfs():
    global f_q,j_q,res
    while True:
        res += 1
        temp = []
        while f_q:
            x,y = f_q.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<r and 0<=ny<c:
                    if A[nx][ny]=='.' or A[nx][ny] =='$':
                        temp.append((nx,ny))
                        A[nx][ny] = 'F'
        f_q = deque(temp)
        
        temp = []
        while j_q:
            x,y = j_q.popleft()
            if x==0 or y==0 or x==r-1 or y==c-1:
                return res
            
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<r and 0<=ny<c:
                    if A[nx][ny]=='.':
                        temp.append((nx,ny))
                        A[x][y] = '$'
                        A[nx][ny] = 'J'
        j_q = deque(temp)
        
        if not j_q:
            return False

r,c = map(int,input().split())
A = [] # 맵 저장
res = 0 # 결과
f_q, j_q = deque(), deque()
for i in range(r):
    tmp = list(input().rstrip())
    A.append(tmp)
    for j in range(c):
        if tmp[j] == 'J':
            j_q.append((i,j))
            
        elif tmp[j] == 'F':
            f_q.append((i,j))
            
            

dx = [1,0,-1,0]
dy = [0,1,0,-1]

if bfs():
    print(res)
else:
    print("IMPOSSIBLE")

