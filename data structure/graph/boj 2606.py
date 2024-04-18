# 1번 컴퓨터가 바이러스에 걸리면 
# 이에 연결된 모든 컴퓨터는 웜 바이러스에 걸림

from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
m = int(input()) # 연결된 컴퓨터 쌍 수
A = [[] for _ in range(n+1)]
vis = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)

def DFS(x):
    global cnt
    vis[x] = True
    for i in A[x]:
        if not vis[i]:
            cnt += 1
            DFS(i)
cnt = 0
DFS(1)
print(cnt)