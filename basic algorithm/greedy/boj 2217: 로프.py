import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]
A.sort()

now = A[0]*n
for i in range(1,n):
    if A[i]*(n-i) > now:
        now = A[i]*(n-i)

print(now)