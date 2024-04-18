n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []
used = [False]*(10001)

def back():
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(len(A)):
        if A[i] not in ans:
            ans.append(A[i])
            back()
            ans.pop()
            
back()