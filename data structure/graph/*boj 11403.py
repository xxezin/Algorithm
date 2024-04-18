import sys
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n)]
for i in range(n):
    A[i] = list(map(int,input().split()))

def DFS(x):
    for i in range(n):
        if check[i] == 0 and A[x][i] == 1:
            check[i] = 1
            DFS(i)

check = [0 for _ in range(n)]
for i in range(n):
    DFS(i)
    print(*check)
    check = [0 for _ in range(n)]