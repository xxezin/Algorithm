import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
      
n,m = map(int,input().split())
tmp = list(map(int,input().split()))
relation = [[] for _ in range(n+1)]
superior = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for i in range(n):
    if tmp[i] == -1:
        continue
    relation[tmp[i]].append(i+1)
    superior[i+1] = tmp[i]

good = []
for _ in range(m):
    i,w = map(int,input().split())
    answer[i] += w
    
def DFS(now):
    answer[now] += answer[superior[now]]
    if relation[now]:
        for nxt in relation[now]:
            DFS(nxt)
            
DFS(1)
print(*answer[1:])
