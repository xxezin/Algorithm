import sys
input = sys.stdin.readline

n = int(input())
S = [[0,0,0] for _ in range(n+1)]
for i in range(1,n+1):
    S[i] = list(map(int,input().split()))
D = [[0,0,0] for _ in range(n+1)]

D[1][0] = S[1][0]
D[1][1] = S[1][1]
D[1][2] = S[1][2]

for k in range(2,n+1):
    D[k][0] = min(D[k-1][1],D[k-1][2]) + S[k][0]
    D[k][1] = min(D[k-1][0], D[k-1][2]) + S[k][1]
    D[k][2] = min(D[k-1][0],D[k-1][1]) + S[k][2]

print(min(D[k]))