m,n = map(int,input().split())
A = list(map(int,input().split()))

s,e = 1,max(A)
ans = 0
while s <= e:
    mid = (s+e)//2
    snack = 0
    for i in range(n):
        snack += A[i]//mid
        
    if snack >= m:
        ans = max(ans,mid)
        s = mid+1
    else:
        e = mid-1

if ans > 0:
    print(ans)
else:
    print(0)