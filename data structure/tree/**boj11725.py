import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

## BFS
# def BFS():
#     while q:
#         now = q.popleft()
#         for i in tree[now]:
#             if not parent[i]:
#                 q.append(i)
#                 parent[i] = now
    
#     return parent
    
# n = int(input())
# tree = [[] for _ in range(n+1)]
# parent = [None for _ in range(n+1)]

# # v개의 정점을 가진 트리는 v-1개의 간선을 가진다
# for _ in range(n-1):
#     u,v = map(int,input().split())
#     tree[v].append(u)
#     tree[u].append(v)

# q = deque(tree[1])
# for i in tree[1]:
#     parent[i] = 1

# BFS()

# for i in range(2,n+1):
#     print(parent[i])


## 비재귀 DFS
# def DFS():
#     while stack:
#         now = stack.pop()
#         for i in tree[now]:
#             if not parent[i]:
#                 stack.append(i)
#                 parent[i] = now

# n = int(input())
# tree = [[] for _ in range(n+1)]
# parent = [None for _ in range(n+1)]

# # v개의 정점을 가진 트리는 v-1개의 간선을 가진다
# for _ in range(n-1):
#     u,v = map(int,input().split())
#     tree[v].append(u)
#     tree[u].append(v)

# stack = tree[1]
# for i in tree[1]:
#     parent[i] = 1
    
# DFS()
    
# for i in range(2,n+1):
#     print(parent[i])


# 재귀 DFS
def DFS(v):
    for i in tree[v]:
        if not parent[i]:
            parent[i] = v
            DFS(i)
    
n = int(input())
tree = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]

# v개의 정점을 가진 트리는 v-1개의 간선을 가진다
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[v].append(u)
    tree[u].append(v)
    
DFS(1)
for i in range(2,n+1):
    print(parent[i])