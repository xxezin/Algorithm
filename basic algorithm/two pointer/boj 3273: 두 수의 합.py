n = int(input())
A = list(map(int,input().split()))
A.sort() # 정렬되어 있어야 투포인터 사용 가능한듯
x = int(input())

l,r = 0,n-1
ans = 0
while l < r:
    if A[l]+A[r] == x:
        ans +=1
        r -=1
    elif A[l]+A[r] < x:
        l +=1
    elif A[l]+A[r] > x:
        r -=1


print(ans)