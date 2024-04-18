import sys
input = sys.stdin.readline

tmp = list(map(str,input().split()))
n = int(tmp[0])
A = []
A += tmp[1:]
while len(A) < n:
    tmp = list(map(str,input().split()))
    A += tmp

for i in range(len(A)):
    A[i] = int(A[i][::-1])
A.sort()
print('\n'.join(map(str,A)))