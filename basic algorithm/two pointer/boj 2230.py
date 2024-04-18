import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = [int(input()) for _ in range(n)]
A.sort() # 투포인터는 정렬된 상태에서!

l,r = 0,0
ans = sys.maxsize
while r != n:
    tmp = A[r]-A[l]
    if tmp < m:
        r += 1
    elif tmp == m:
        ans = min(ans,tmp)
        r += 1
    else:
        ans = min(ans,tmp)
        l += 1

print(ans)