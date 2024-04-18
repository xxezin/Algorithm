import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

D = [1]*n
B = [[A[i]] for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if A[i] > A[j] and D[i] < D[j]+1:
            D[i] = D[j]+1
            B[i] = B[j]+[A[i]]

m = max(D)
print(m)
print(*B[D.index(m)]) # max가 처음으로 등장하는 idx 반환