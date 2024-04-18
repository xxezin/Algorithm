n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
used = [False]*n
ans = []

def func(start):
    prev = 0
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start,n):
        if not used[i] and prev != A[i]:
            ans.append(A[i])
            used[i] = True
            prev = A[i]
            func(i+1)
            ans.pop()
            used[i] = False
        
func(0)

