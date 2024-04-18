import sys
input = sys.stdin.readline
       
def DFS(v):
    tree[v] = -2 # 노드 삭제
    for i in range(n): # 삭제하는 노드의 자식 노드가 있으면 그것도 삭제
        if v == tree[i]:
            DFS(i)
 
n = int(input()) # 트리의 노드 갯수
tree = list(map(int,input().split())) # 부모 노드
erase = int(input()) # 지울 노드

DFS(erase)

cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in tree: # 삭제한 노드가 아니고, 누군가의 부모 노드가 아니면
        cnt += 1
        
print(cnt)