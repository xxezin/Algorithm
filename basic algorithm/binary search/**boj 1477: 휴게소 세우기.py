import sys
input = sys.stdin.readline

n,m,l = map(int,input().split()) # 현재 개수, 지으려는 개수, 고속도로 길이

A = [0]+list(map(int,input().split()))+[l] # 시작점, 휴게소 위치, 끝점
A.sort()

start,end = 1,l-1
result = 0

while start <= end:
    cnt = 0
    mid = (start+end)//2

    for i in range(1,len(A)):
        if A[i]-A[i-1] > mid:
            cnt += (A[i]-A[i-1]-1)//mid
    
    if cnt > m:
        start = mid+1
    else:
        end = mid-1
        result = mid

print(result)
