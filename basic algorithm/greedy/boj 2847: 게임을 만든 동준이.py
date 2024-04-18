import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]

ans = 0
for i in range(n-1,0,-1):
    while A[i] <= A[i-1]:
        A[i-1] -=1
        ans +=1

print(ans)