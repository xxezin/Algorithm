import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    d_line, cup = map(int,input().split())
    A.append((d_line,cup))

A.sort()
heap = []

for i in A:
    heapq.heappush(heap,i[1])
    if i[0] < len(heap): # 최소 힙 구현으로 자연스레 같은 날짜 중 작은 애들을 팝
        heapq.heappop(heap)

print(sum(heap))