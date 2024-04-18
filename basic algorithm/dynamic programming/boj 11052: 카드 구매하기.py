import sys
input = sys.stdin.readline

n = int(input())
P = [0] + list(map(int,input().split()))

D = [0]*(1001)
D[1] = P[1]

for i in range(2,n+1):
    k=0
    while k<=i:
        D[i] = max(D[i],P[i-k]+D[k])
        k+=1

print(D[n])