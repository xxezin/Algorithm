from collections import deque
import sys
input = sys.stdin.readline

# 보드 만들기
n = int(input())
D = [[0]*(n) for _ in range(n)]

# 사과를 놓기
k = int(input())
for _ in range(k):
    x,y = map(int,input().split())
    D[x-1][y-1] = 2

t = int(input())
dirDict = dict() # 
for _ in range(t):
    x,c = input().split()
    dirDict[int(x)] = c

q = deque() # 뱀의 몸을 나타냄
x,y = 0,0 # 뱀의 초기 위치
q.append((x,y))
D[x][y] = 1

dir = 0 # 뱀의 초기 방향. 오른쪽
# 방향 변환 함수
def turn(a):
    global dir
    if a == 'L':
        dir = (dir-1)%4
    else:
        dir = (dir+1)%4

dx = [0,1,0,-1]
dy = [1,0,-1,0]
time = 0
while True:
    time += 1
    x += dx[dir]
    y += dy[dir]

    if x<0 or x>=n or y<0 or y>=n:
        break

    if D[x][y] == 2: # 사과가 있으면 몸이 커짐
        D[x][y] = 1 # 뱀의 몸이 존재
        q.append((x,y))
        if time in dirDict: # 시간이 지날 때마다 방향 변환 확인
            turn(dirDict[time])
    
    elif D[x][y] == 0 : # 사과가 없으면 몸이 줄어들음
        D[x][y] = 1
        q.append((x,y))
        tx,ty = q.popleft()
        D[tx][ty] = 0
        if time in dirDict:
            turn(dirDict[time])

    else:
        break

print(time)

