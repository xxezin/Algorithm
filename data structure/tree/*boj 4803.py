import sys
input = sys.stdin.readline
from collections import deque

def BFS(x):
    flag = False
    q = deque()
    q.append(x)
    
    while q:
        now = q.popleft()
        if vis[now]: # 이미 방문했다면
            flag = True
        vis[now] = True
        
        for i in tree[now]:
            if not vis[i]:
                q.append(i)
    return flag
   
num = 1             
while True:
    n,m = map(int,input().split())
    if n == m == 0:
        break
    tree = [[] for _ in range(n+1)] # 트리
    vis = [False]*(n+1) # 정점 방문 여부
        
    for _ in range(m):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
        # if u == v:
        #     continue
    
    t_cnt = 0 # 트리 갯수
    for i in range(1,n+1): # 연결되지 않은 정점마다 BFS 실행
        if not vis[i]:
            if not BFS(i):
                t_cnt += 1

    if t_cnt == 0:
        print("Case {0}: No trees.".format(num))
    elif t_cnt == 1:
        print("Case {0}: There is one tree.".format(num))
    else:
        print("Case {0}: A forest of {1} trees.".format(num,t_cnt))
    num += 1