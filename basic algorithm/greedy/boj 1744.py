import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
mh, ph = [],[]
one, zero = 0,0

for _ in range(n):
    a = int(input())
    if a < 0:
        heapq.heappush(mh,a)
    elif a > 1:
        heapq.heappush(ph,-a)
    elif a==0:
        zero += 1
    else:
        one += 1
        
   
answer = 0 
while mh:
    if len(mh) >= 2:
        a = heapq.heappop(mh)
        b = heapq.heappop(mh)
        answer += a*b
        continue
    
    if zero:
        heapq.heappop(mh)
    else:
        answer += heapq.heappop(mh)
    
while ph:
    if len(ph) >= 2:
        a = heapq.heappop(ph)
        b = heapq.heappop(ph)
        answer += a*b
        continue
    answer += -heapq.heappop(ph)

if one:
    answer += one
print(answer)