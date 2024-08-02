import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if heap:
            print(heapq.heappop(heap)[1])
            continue
        
        print(0)
        continue
    heapq.heappush(heap, (abs(a),a))
