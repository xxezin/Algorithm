from bisect import bisect_left
n,m = map(int,input().split())
A = sorted(list(map(int,input().split())))

s,e = 0,max(A)
answer = 0

while s <= e:
    mid = (s+e)//2
    tree = 0
    idx = bisect_left(A,mid)
    for i in range(idx,n):
        tree += A[i]-mid
        
    if tree >= m:
        answer = max(answer,mid)
        s = mid+1
    else:
        e = mid-1

print(answer)