import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def subtree(u):
    global vis, S, tree
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

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

vis = [0]*(n+1)
S = [0]*(n+1)

subtree(r)

for _ in range(q):  
    print(S[int(input())])