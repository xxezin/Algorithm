import math
n,k = map(int,input().split())
A = [i for i in range(n+1)]
A[1] = 0

cnt = 0
for i in range(2,n+1):
    for j in range(i,n+1,i):
        if A[j]:
            A[j] = 0
            cnt += 1
            if cnt == k:
                print(j)
                break
