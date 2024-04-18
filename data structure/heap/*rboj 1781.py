import sys
import heapq
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    day,cup = map(int,input().split())
    A.append((day,cup))

A.sort()
heap = []

for i in A:
    heapq.heappush(heap,i[1]) # 일단 최소힙에 넣고
    if i[0] < len(heap): # 그 날짜에서 작은 값들 다 pop
        heapq.heappop(heap)

print(sum(heap))