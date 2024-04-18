n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def func(k):
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(n):
        ans.append(A[i])
        func(i+1)
        ans.pop()

func(0)