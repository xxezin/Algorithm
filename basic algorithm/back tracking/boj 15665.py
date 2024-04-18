n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def back():
    if len(ans) == m:
        print(*ans)
        return
    
    prev = 0
    for i in range(n):
        if prev != A[i]:
            ans.append(A[i])
            prev = A[i]
            back()
            ans.pop()

back()