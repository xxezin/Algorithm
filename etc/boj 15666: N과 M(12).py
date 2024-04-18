n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def func(start):
    prev = 0
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start-1,n):
        if prev != A[i]:
            ans.append(A[i])
            prev = A[i]
            func(i+1)
            ans.pop()

func(1)
