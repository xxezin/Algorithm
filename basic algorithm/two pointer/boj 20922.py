n,k = map(int,input().split())
A = list(map(int,input().split()))

used = [0]*(200001)
l,r = 0,0
ans = 0

while l<=r and r<n:
    if used[A[r]] < k:
        used[A[r]] += 1
        ans = max(ans,r-l+1)
        r += 1
    
    else:
        while used[A[r]] >= k:
            used[A[l]] -=1
            l += 1

print(ans)