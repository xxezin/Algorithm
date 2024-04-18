import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v,cycle):
    global answer
    
    vis[v] = True
    cycle.append(v)
    nxt = A[v] # 다음 방문
    
    if vis[nxt]: # 방문하는 애가 이미 사이클에 있으면
        if nxt in cycle:
            answer -= (len(cycle) - cycle.index(nxt))
            return
        
    else:
        dfs(nxt,cycle)
    

T = int(input())
for _ in range(T):
    n = int(input())
    A = [0]+list(map(int,input().split()))
    vis = [False]*(n+1)
    answer = n
    for i in range(1,n+1):
        if not vis[i]:
            dfs(i,[])
            
    print(answer)