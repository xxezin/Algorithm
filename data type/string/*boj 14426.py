import sys
from bisect import bisect
input = sys.stdin.readline

n,m = map(int,input().split())
A = [input().rstrip() for _ in range(n)]
B = [input().rstrip() for _ in range(m)]
A.sort()

cnt = 0
for i in range(m):
    tmp = min(n-1,bisect(A,B[i]))
    
    if A[tmp].startswith(B[i]):
        cnt += 1
    elif A[tmp-1].startswith(B[i]):
        cnt += 1
        
print(cnt)