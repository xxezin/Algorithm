import sys
sys.setrecursionlimit(10**6)

r,c = map(int,input().split())
graph = []
for _ in range(r):
    tmp = list(input().rstrip())
    graph.append(tmp)

answer = 0
alpha = set()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(graph):
    result = 1
    queue = set([(0,0,graph[0][0])])
    while queue:
        x,y,vis = queue.pop()
        result = max(result,len(vis))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if not graph[nx][ny] in vis:
                    queue.add((nx,ny,vis+graph[nx][ny]))
    
    return result

answer = bfs(graph)
print(answer)