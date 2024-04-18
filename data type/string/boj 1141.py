import sys
input = sys.stdin.readline

n = int(input())
A = [input().rstrip() for _  in range(n)]
A.sort(key=lambda x:len(x))

cnt = n
for i in range(n):
    for j in range(i+1,n):
        if A[j].startswith(A[i]):
            cnt -=1 # A[i]는 누군가의 접두어니 cnt - 1
            break

print(cnt)