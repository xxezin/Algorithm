import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

# # 재귀 DFS 구현
# def DFS(graph,vertex,visited):
#     for i in graph[vertex]:
#         # 만약 아직 방문하지 않았다면
#         if not visited[i]:
#             visited[i] = vertex
#             DFS(graph,i,visited)

# DFS(tree,1,parent) # 루트는 1이니 루트부터

# # 비재귀 DFS 구현
# def DFS():
#     while stack:
#         now = stack.pop()
#         for i in tree[now]:
#             if not parent[i]:
#                 stack.append(i)
#                 parent[i] = now
    
# for i in tree[1]: # 루트의 자식노드 처리
#     parent[i] = 1
# stack = deque(tree[1])
# DFS()

# # BFS 구현
# def BFS():
#     while q:
#         now = q.popleft()
#         for i in tree[now]:
#             if not parent[i]:
#                 q.append(i)
#                 parent[i] = now
        
# for i in tree[1]: # 루트의 자식 노드 처리
#     parent[i] = 1
# q = deque(tree[1])
# BFS() 
    
for i in range(2,n+1):
    print(parent[i])