import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int,input().split()))
A.sort()

s,e = 0,n-1
cnt = 0

while s < e:
    tmp = A[s] + A[e]
    if tmp == m:
        cnt += 1
        s += 1
        e -= 1

    elif tmp > m:
        e -= 1

    else:
        s += 1
    
print(cnt)