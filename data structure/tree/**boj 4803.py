import sys
from collections import deque
input = sys.stdin.readline

def BFS(now):
    flag = False
    
    q = deque([now])
    while q:
        now = q.popleft()
        if vis[now]: # 방문한 적이 있는지. 순환 여부 체크
            flag = True
            
        vis[now] = True
        
        for i in tree[now]: # 연결된 정점 탐색
            if not vis[i]:
                q.append(i)

    return flag

T = 1
while True:
    n,m = map(int, input().split())
    if n == 0:
        break
    
    tree = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    tree_cnt = 0
    vis = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if not vis[i]:
            if not BFS(i):
                tree_cnt += 1
            
    if tree_cnt == 0:
        print(f"Case {T}: No trees.")
    elif tree_cnt == 1:
        print(f"Case {T}: There is one tree.")
    else:
        print(f"Case {T}: A forest of {tree_cnt} trees.")
    
    T += 1