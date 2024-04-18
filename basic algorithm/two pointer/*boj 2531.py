import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
A = []
for i in range(n):
    A.append(int(input()))
A += A[:k-1]

ans = 0
for i in range(n):
    eat = set(A[i:i+k] + [c])
    ans = max(ans,len(eat))
    
print(ans)