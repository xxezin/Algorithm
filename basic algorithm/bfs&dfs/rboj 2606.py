n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)

def dfs(v):
    global cnt
    vis[v] = True
    cnt += 1
    for i in A[v]:
        if not vis[i]:
            dfs(i)

cnt = 0
vis = [False]*(n+1)
dfs(1)
print(cnt-1)