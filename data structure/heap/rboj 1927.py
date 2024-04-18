import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)
            
    else:
        heapq.heappush(pq,tmp)