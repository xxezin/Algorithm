import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    heapq.heapify(A)

    result = []
    while len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        heapq.heappush(A,a+b)
        result.append(a+b)
    print(sum(result))