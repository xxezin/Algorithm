import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    tmp = list(input().split())
    A.append((tmp[0],int(tmp[1]),int(tmp[2]),int(tmp[3])))

A.sort(key=lambda x:(x[3],x[2],x[1]))

print(A[-1][0])
print(A[0][0])