# # 우선순위 큐로 구현 (시간초과)
# from queue import PriorityQueue
# import sys
# input = sys.stdin.readline

# n = int(input())
# q = PriorityQueue(maxsize=n)

# for i in range(n):
#     tmp = list(map(int,input().split()))
#     for j in tmp:
#         if q.qsize() < n :
#             q.put(j)
#         else:
#             now = q.get()
#             if now < j:
#                 q.put(j)
#             else:
#                 q.put(now)
                
# print(q.get())

# 힙으로 구현
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in tmp:
        if len(heap) < n:
            heapq.heappush(heap,i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap,i)

print(heap[0])