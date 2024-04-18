import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
A.sort(key=lambda x:x[0])

l = A[0][0]
r = A[0][1]
len = 0
for i in range(1,n):
    if r < A[i][0]:
        len += (r-l)
        l = A[i][0]
        r = A[i][1]

    elif A[i][0] <= r and A[i][1] >= r:
        r = A[i][1]
        
len += (r-l)
print(len)