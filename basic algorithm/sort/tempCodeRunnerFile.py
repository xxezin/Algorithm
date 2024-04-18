import sys
input = sys.stdin.readline

n = int(input())
A = [[0,0] for _ in range(n)]
for i in range(n):
    A[i][0] = input().split()
    A[i][1] = i

A.sort()

for i in range(1,n):
    if A[i-1][0][0]==A[i][0][0]:
        if A[i-1][1] > A[i][1]:
            A[i-1],A[i] = A[i],A[i-1]


for i in range(n):
    print(' '.join(map(str,A[i][0])))