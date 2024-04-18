n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def back(start):
    if len(ans) == m:
        print(*ans)
        return
    
    prev = 0
    for i in range(start,n):
        if prev != A[i]:
            prev = A[i]
            ans.append(A[i])
            back(i)
            ans.pop()
            
back(0)