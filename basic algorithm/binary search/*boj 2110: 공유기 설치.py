import sys
input = sys.stdin.readline

n,c = map(int,input().split())
A = [int(input()) for _ in range(n)]
A.sort()

# 거리!를 설정해 최대 거리를 출력한다.
start,end = 1,A[-1]
ans = 0

while start <= end:
    mid = (start+end)//2
    curr = A[0]
    cnt = 1

    for i in range(1,n):
        if A[i]-curr >= mid:
            cnt +=1
            curr = A[i]

    if cnt >= c:
        ans = mid
        start = mid +1
    else:
        end = mid-1

print(ans)