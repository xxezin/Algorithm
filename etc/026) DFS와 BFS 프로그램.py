from collections import deque
N,M,Start = map(int,input().split())
A = [[] for _ in range(N+1)]

# 노드 인접리스트 저장
for _ in range(M):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

# 노드가 방문할 수 있는 노드 오름차순 정렬
for i in range(N+1):
    A[i].sort()

# DFS
def DFS(now):
    print(now,end=' ')
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i)


# BFS
def BFS(now):
    queue = deque()
    queue.append(now)
    visited[now] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node,end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


visited = [False]*(N+1)
DFS(Start)
print()
visited = [False]*(N+1)
BFS(Start)
