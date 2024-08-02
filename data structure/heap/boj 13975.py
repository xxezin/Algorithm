import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    heap = list(map(int,input().split()))
    heapq.heapify(heap)
    
    result = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        result += a+b
        
    print(result)