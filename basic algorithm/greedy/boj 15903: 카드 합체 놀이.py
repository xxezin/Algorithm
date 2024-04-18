import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
heapq.heapify(A) # 힙으로 저장

while m:

    a = heapq.heappop(A)
    b = heapq.heappop(A)
    heapq.heappush(A,a+b)
    heapq.heappush(A,a+b)
    m -= 1

print(sum(A))