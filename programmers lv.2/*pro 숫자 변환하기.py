from collections import deque
def solution(x, y, n):
    answer = 0
    q = deque()
    q.append((x,0))
    vis = set()
    vis.add(x)
    
    while q:
        v,cnt = q.popleft()
        if v == y:
            return cnt
        
        for k in (v*2,v*3,v+n):
            if k <=y and k not in vis:
                q.append((k,cnt+1))
                vis.add(k)
                
    return -1