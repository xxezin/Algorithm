n = int(input())
A = list(map(int,input().split()))

l,r = 0,0
cnt = 0

while r < n:
    if l-r == 0:
        cnt += 1
        r += 1

    elif A[r] in A[l:r]:
        l += 1
        
    else:
        cnt +=1
        r += 1

print(cnt)