import sys
sys = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split()))) 

ans = 0

def func(k):
    global ans

    if k==n:
        cnt = 0
        for i in range(n):
            if A[i][0]<=0:
                cnt+=1
        ans = max(ans,cnt)
        return
    
    if A[k][0]<=0:
        func(k+1)
        return
    
    isAll = True
    for i in range(n):
        if i==k:
            continue
        if A[i][0]>0:
            isAll = False
            break
    if isAll:
        ans = max(ans,n-1)
        return

    for i in range(n):
        if i==k:
            continue
        if A[i][0] <= 0:
            continue

        # 때려봐
        A[k][0]-=A[i][1]
        A[i][0]-=A[k][1]
        func(k+1)

        # 복구
        A[k][0]+=A[i][1]
        A[i][0]+=A[k][1]

func(0)
print(ans)