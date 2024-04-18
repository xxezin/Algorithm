n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def back(start):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start,n):
        ans.append(A[i])
        back(i)
        ans.pop()
        
back(0)