import sys
sys.setrecursionlimit(5000000) # ?
input = sys.stdin.readline

def DFS(x,y):
    dx = [1,1,-1,-1,1,-1,0,0]
    dy = [0,1,0,1,-1,-1,1,-1]

    A[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if A[nx][ny] == 1:
                DFS(nx,ny)

while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    cnt = 0
    A = []
    for _ in range(m):
        A.append(list(map(int,input().split())))
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                DFS(i,j)
                cnt += 1
    print(cnt)