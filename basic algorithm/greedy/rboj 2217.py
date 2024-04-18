import sys
input = sys.stdin.readline

n = int(input())
A = list(int(input()) for _ in range(n))
A.sort()

M = 0
for i in range(n):
    M = max(M,A[i]*(n-i))

print(M)