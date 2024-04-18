import sys
inpu = sys.stdin.readline

A = list(map(int,input()))
n = len(A)

ans_0, ans_1 = 0,0
if A[0] == 0:
    ans_0 +=1
elif A[0] == 1:
    ans_1 +=1


for i in range(n-1):
    if A[i] != A[i+1]:
        if A[i+1] == 0:
            ans_0 +=1
        elif A[i+1] == 1:
            ans_1 +=1

print(min(ans_0,ans_1))