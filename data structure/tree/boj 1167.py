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
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(1,len(tmp)-1,2):
        if tmp[i] == -1:
            break
        
        tree[tmp[0]].append([tmp[i],tmp[i+1]])
        
dist = [-1]*(n+1)
dist[1] = 0
dfs(1,0)
start = dist.index(max(dist))

dist = [-1]*(n+1)
dist[start] = 0
dfs(start,0)

print(max(dist))
# [[], 
#  [[3, 2]], 
#  [[4, 4]], 
#  [[1, 2], [4, 3]], 
#  [[2, 4], [3, 3], [5, 6]], 
#  [[4, 6]]]

