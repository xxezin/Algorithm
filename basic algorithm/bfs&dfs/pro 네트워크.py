def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n)] # 인접 리스트 생성
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                adj[i].append(j)
    vis = [False]*(n)
    
    for i in range(n):
        if not vis[i]:
            dfs(adj,vis,i)
            answer += 1
    return answer
        
    
def dfs(adj,vis,v):
    vis[v] = True
    
    for i in adj[v]:
        if not vis[i]:
            dfs(adj,vis,i)

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))