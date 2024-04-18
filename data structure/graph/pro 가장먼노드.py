from collections import deque
def solution(n, edge):
    A = [[] for _ in range(n+1)]
    for i,j in edge:
        A[i].append(j)
        A[j].append(i)
    
    def BFS(x):
        q = deque()
        q.append(x)
        
        vis = [-1]*(n+1)
        vis[x] = 0
        while q:
            now = q.popleft()
            for i in A[now]:
                if vis[i] == -1:
                    vis[i] = vis[now] + 1
                    q.append(i)
        return vis
    
    tmp = BFS(1)
    M = max(tmp)
    cnt = 0
    for i in tmp:
        if i==M:
            cnt += 1
    return cnt
    

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])