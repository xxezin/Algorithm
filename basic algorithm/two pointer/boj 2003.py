n,m = map(int,input().split())
A = list(map(int,input().split()))

l,r,cnt = 0,0,0
sum = A[0]

while True:
    if sum < m:
        r += 1
        if r == len(A):
            break
        sum += A[r]
        
    elif sum == m:
        cnt += 1
        sum -= A[l]
        l += 1
        
    else:
        sum -= A[l]
        l += 1

print(cnt)