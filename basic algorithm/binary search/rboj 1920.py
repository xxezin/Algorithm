import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int,input().split())))
m = int(input())
B = list(map(int,input().split()))

for i in range(m):
    s,e = 0,n-1
    while s<=e:
        mid = (s+e)//2
        if B[i] == A[mid]:
            print(1)
            break
        else:
            if B[i] < A[mid]:
                e = mid-1
            else:
                s = mid+1
    else:
        print(0)