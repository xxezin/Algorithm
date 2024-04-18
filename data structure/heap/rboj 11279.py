import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []

# heapq 최대힙 구현 1
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(pq,(-tmp,tmp))

# # heapq 최대힙 구현 2
# for _ in range(n):
#     tmp = int(input())
#     if tmp == 0:
#         if pq:
#             print(-heapq.heappop(pq))
#         else:
#             print(0)
            
#     else:
#         heapq.heappush(pq,-tmp)