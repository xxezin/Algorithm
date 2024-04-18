def dfs(depth,idx):
    global n,answer
    if depth == n//2:
        p1,p2 = 0,0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    p1 += s[i][j] # 스타트팀
                elif not visit[i] and not visit[j]:
                    p2 += s[i][j] # 링크팀
                    
        answer = min(answer,abs(p1-p2)) # 차이가 적은것
        return
    
    for i in range(idx,n):
        if not visit[i]:
            visit[i] = 1
            dfs(depth+1,i+1)
            visit[i] = 0
            
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
visit = [0]*(n)
answer = 1e3
dfs(0,0)
print(answer)