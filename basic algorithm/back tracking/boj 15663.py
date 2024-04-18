n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []
used = [False]*n

def back():
    if len(ans) == m:
        print(*ans)
        return
    
    prev = 0
    for i in range(n):
        if not used[i] and prev != A[i]: # 이전 숫자를 기억함으로써 중복 방지
            used[i] = True
            ans.append(A[i])
            prev = A[i]
            back()
            used[i] = False
            ans.pop()

back()