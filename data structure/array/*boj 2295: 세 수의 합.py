import sys
input = sys.stdin.readline

n = int(input())
A  = [int(input()) for _ in range(n)]
A.sort()

A_sum = set()
for x in A:
    for y in A:
        A_sum.add(x+y)

answer = 0
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if A[i]-A[j] in A_sum:
            answer = max(A[i],answer)

print(answer)