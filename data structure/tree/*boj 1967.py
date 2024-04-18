# 경로 중 가장 길게 늘어나는 경우, 이 길이를 트리의 지름이라고 함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node,weight):
    for n,w in tree[node]:
        if dist[n] == -1:
            dist[n] = weight + w
            dfs(n,weight+w)
            
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p,c,w = map(int,input().split()) # 부모노드, 자식노드, 가중치
    tree[p].append([c,w]) # 부모 노드에 자식노드, 가중치 할당
    tree[c].append([p,w])

dist = [-1]*(n+1)
dist[1] = 0
dfs(1,0) # 루트에서 가장 먼 리프노드 찾기

start = dist.index(max(dist)) # 루트에서 가장 먼 리프노드 저장
dist = [-1]*(n+1)
dist[start] = 0 # 루트에서 가장 먼 리프노드부터 시작해 가장 먼 리프노드 찾기
dfs(start,0)

print(max(dist))
