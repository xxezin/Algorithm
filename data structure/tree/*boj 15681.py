import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def subtree(u):
    global vis,tree,S
    if vis[u]:
        return 0
    vis[u] = 1
    
    cnt = 1
    for v in tree[u]:
        if not vis[v]:
            cnt += subtree(v)
            
    S[u] = cnt
    return cnt

n,r,q = map(int,input().split())

tree = [[] for _ in range(n+1)] # 트리 입력
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

vis = [0]*(n+1)
S = [0]*(n+1)

subtree(r)
for _ in range(q):
    print(S[int(input())])
