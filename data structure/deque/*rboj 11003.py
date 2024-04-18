from collections import deque
import sys
input = sys.stdin.readline

n,l = map(int,input().split())
A = list(map(int,input().split()))
q = deque()

for i in range(n):
    while q and q[-1][0] > A[i]:
        q.pop()
        
    q.append((A[i],i))
    
    if q[-1][1] - q[0][1] >= l:
        q.popleft()

    print(q[0][0],end=' ')