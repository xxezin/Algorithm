import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict

# 중위 순환으로 구현
def inOrd(now,layer):
    global idx,cnt
    if tree[now][0] != -1:
        inOrd(tree[now][0],layer+1)
    layers[layer].append(cnt)
    cnt += 1
    if tree[now][1] != -1:
        inOrd(tree[now][1],layer+1)
        
n = int(input())
tree = [[] for _  in range(n+1)]
depth =  [1]*(n+1)
rootCandidate = [0]*(n+1)
for _ in range(n):
    p,lc,rc = map(int,input().split()) # 부모, 왼/오 자식
    tree[p] = [lc,rc]
    if lc != -1:
        rootCandidate[lc] += 1
    if rc != -1:
        rootCandidate[rc] += 1


# 루트 노드 찾기
for i in range(1,n+1):
    if rootCandidate[i] == 0: # 누군가의 자식이 아닌 애가
        root = i

layers = defaultdict(list)
cnt = 1
inOrd(root,1)

L,W = 0,0 # layer과 width
for key in sorted(layers):
    values = layers[key]
    width = max(values) - min(values) + 1
    
    if W < width:
        L,W = key,width
        
print(L, W)