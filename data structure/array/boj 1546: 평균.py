n = int(input())
A = list(map(int,input().split()))
M = max(A)

ans = 0
for i in A:
    ans += (i/M)*100

print(ans/n)