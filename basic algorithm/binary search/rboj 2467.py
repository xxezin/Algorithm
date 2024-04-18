n = int(input())
A = list(map(int,input().split()))
A.sort()

s,e = 0,n-1
ans = 2000000001
min_v,max_v = 0,0
while s < e:
    tmp = A[s] + A[e]
    if tmp == 0:
        min_v,max_v = A[s],A[e]
        break
    else:
        if tmp < 0:
            if abs(tmp) < ans:
                ans = min(ans,abs(tmp))
                min_v,max_v = A[s],A[e]
            s += 1
            
        else:
            if tmp < ans:   
                ans = min(ans,abs(tmp))
                min_v,max_v = A[s],A[e]
            e -= 1

print(min_v,max_v)