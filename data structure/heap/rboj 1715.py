import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    heapq.heappush(pq,int(input()))

ans = 0
while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    ans += (a+b)
    heapq.heappush(pq,a+b)
    
print(ans)