import sys
import heapq
input = sys.stdin.readline

n = int(input())
left,right = [],[] # 힙 두개 구현
for i in range(n):
    x = int(input())
    if len(left) == len(right): # 왼쪽 힙부터 채움
        heapq.heappush(left,-x)
    else:
        heapq.heappush(right,x)
        
    if right and right[0] < -left[0]: # left : 작은 값을 최대 힙으로, right : 큰 값을 최소 힙으로
        lv = heapq.heappop(left)
        rv = heapq.heappop(right)
        
        heapq.heappush(right,-lv)
        heapq.heappush(left,-rv)

    print(-left[0])