n,m = map(int,input().split())
A = list(map(int,input().split()))
D = [0]*n
C = [0]*m

D[0] = A[0]
for i in range(1,n):
    D[i] = D[i-1] + A[i]

answer = 0
for i in range(n):
    remain = D[i] % m
    if remain == 0:
        answer += 1
    C[remain] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i]*(C[i]-1)//2)
    
print(answer)