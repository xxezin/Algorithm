import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input()) # 소설 구성 장수
    A = list(map(int,input().split()))
    heapq.heapify(A)
    
    ans = 0
    while len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        ans += (a+b)
        heapq.heappush(A,a+b)
        
    print(ans)