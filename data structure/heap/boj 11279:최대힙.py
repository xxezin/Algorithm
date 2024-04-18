import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    x = int(input())
    if x == 0:
        if A:
            print(-heapq.heappop(A))
        else:
            print(0)
    else:
        heapq.heappush(A,-x)

