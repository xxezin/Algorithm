n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []
used = [False]*n

def back(start):
    if len(ans) == m:
        print(*ans)
        return
    
    prev = 0
    for i in range(start,n):
        if not used[i] and prev != A[i]:
            used[i] = True
            ans.append(A[i])
            prev = A[i]
            back(i+1)
            used[i] = False
            ans.pop()
            
back(0)
        