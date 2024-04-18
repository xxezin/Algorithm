import sys
input = sys.stdin.readline

k,n = map(int,input().split())
A = sorted(list(int(input()) for _ in range(k)))

s, e = 1, max(A)
while s <= e:
    mid = (s+e)//2
    line = 0
    
    for a in A:
        line += a//mid
    
    if line >= n:
        s = mid+1
    else:
        e = mid-1
print(e) # 중간값으로 했을때 틀림