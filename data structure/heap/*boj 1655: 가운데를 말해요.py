import heapq
import sys
input = sys.stdin.readline

n = int(input())
left,right = [],[]

for i in range(n):
    x = int(input())

    if len(left) == len(right):
        heapq.heappush(left,-x)
    else:
        heapq.heappush(right,x)
    
    if right and right[0] < -left[0]:
        leftValue = heapq.heappop(left)
        rightValue = heapq.heappop(right)

        heapq.heappush(left,-rightValue)
        heapq.heappush(right,-leftValue)

    print(-left[0])