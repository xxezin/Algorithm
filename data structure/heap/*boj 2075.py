import sys, heapq
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in tmp:
        if len(A) < n:
            heapq.heappush(A,i)
            continue
        
        top = heapq.heappop(A)
        if i < top:
            heapq.heappush(A,top)
            continue
        heapq.heappush(A,i)
        
print(heapq.heappop(A))