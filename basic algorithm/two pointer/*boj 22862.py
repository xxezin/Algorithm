n,k = map(int,input().split())
A = list(map(int,input().split()))

end,odd = 0,0
ans = 0
tmp = 0

for start in range(n):
    while odd <= k and end < n:
        if A[end] %2: # 홀수일때
            odd += 1
        else: # 짝수일때
            tmp += 1 # 현재 길이 +1
        end += 1

        if start == 0 and end == n:
            ans = tmp
            break
    
    if odd == k+1:
        ans = max(tmp,ans)
        
    if A[start] %2: # 홀수일때
        odd -= 1
    else:
        tmp -= 1
        
print(ans)