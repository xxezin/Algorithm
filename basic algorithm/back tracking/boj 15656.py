n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def back():
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(n):
        ans.append(A[i])
        back()
        ans.pop()

back()