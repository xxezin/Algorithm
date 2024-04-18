n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
used = [False]*n
ans = [0]*m


def func(k):
    prev = 0
    if k==m:
        print(' '.join(map(str,ans)))
        return
        
    for i in range(n):
        if not used[i] and A[i]!=prev:
            used[i] = True
            ans[k],prev = A[i],A[i]
            func(k+1)
            used[i] = False

func(0)

