from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def dijkstra(graph,start,vis):
    q = []
    heapq.heappush(q,(0,start))
    vis[start] = 0
    
    while q:
        weight, now = heapq.heappop(q)

        if vis[now] < weight: # 만약 현재 값이 weight보다도 작으면 업데이트할 필요 없음
            continue
        
        for new_node, new_weight in graph[now]:
            tmp = new_weight + weight
            if tmp < vis[new_node]:
                vis[new_node] = tmp
                heapq.heappush(q,(tmp,new_node))
                
    return vis


V,E = map(int,input().split())
start = int(input())
A = defaultdict(list) # graph
for _ in range(E):
    u,v,w = map(int,input().split())
    A[u].append((v,w))
B = defaultdict(lambda:float('inf')) # visited

answer = dijkstra(A,start,B)
for i in range(1,V+1):
    if i not in answer:
        print('INF')
    else:
        print(answer[i])