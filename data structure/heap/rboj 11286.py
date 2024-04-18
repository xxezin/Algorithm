import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    tmp = int(input())
    if tmp != 0:
        heapq.heappush(pq,(abs(tmp),tmp))
    else:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)