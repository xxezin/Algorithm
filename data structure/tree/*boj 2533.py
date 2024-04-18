import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    vis[node] = True
    dp[node][0],dp[node][1] = 0,1
    
    for child in tree[node]:
        if not vis[child]:
            dfs(child)
            dp[node][0] += dp[child][1] # 내가 얼리어답터가 아니면 자식이 얼리어답터여야함
            dp[node][1] += min(dp[child][0],dp[child][1]) # 내가 얼리어답터면 자식이 얼리어답터인거랑, 얼리어답터가 아닌거랑 비교해서 최소

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

dp  = [[0]*2 for _ in range(n+1)]
vis = [False]*(n+1)
dfs(1)
print(min(dp[1][0],dp[1][1]))

# 자식이 있으면 자기의 부모가 얼리어답터여야 최소로 구현 가능
# 루트와 리프 사이에 있는 모든 애들이 얼리어답터
# 단, 루트와 바로 연결되어 있지만 자식이 없는 노드는 얼리어답터
# 전체 깊이가 2인 경우에는 루트가 얼리어답터
