n,s = map(int,input().split())
A = list(map(int,input().split()))

l,r = 0,0
sum = A[0]
ans = 100001
while True:
    if sum < s: # 부분합이 s보다 작으면
        r += 1
        if r == n:
            break
        sum += A[r]
    
    else: # 부분합이 s와 같거나 크면
        ans = min(ans,r-l+1)
        sum -= A[l]
        l += 1

if ans==100001:
    print(0)
else:
    print(ans)