import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
A.sort()
x = int(input())

i,j = 0,n-1
cnt = 0
while i < j:
    tmp = A[i]+A[j]
    if tmp == x:
        cnt += 1
        i += 1
        
    elif tmp < x:
        i += 1
    
    else:
        j -= 1
        
print(cnt)