import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    tmp = list(input().rstrip().split())
    A.append([str(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])])

A.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in A:
    print(i[0])