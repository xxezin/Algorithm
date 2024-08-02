import sys, heapq
input = sys.stdin.readline

n = int(input())
lh = []
rh = []
for _ in range(n):
    now = int(input())
    if len(lh) == len(rh):
        heapq.heappush(lh, -now)
    else:
        heapq.heappush(rh, now)
    
    if rh and rh[0] < -lh[0]:
        lv = heapq.heappop(lh)
        rv = heapq.heappop(rh)
        
        heapq.heappush(lh, -rv)
        heapq.heappush(rh, -lv)
    
    print(-lh[0])