import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    D = [list(map(int,input().split())) for _ in range(2)]

    if n>=2:
        D[0][1] += D[1][0]
        D[1][1] += D[0][0]
        for i in range(2,n):
            D[0][i] += max(D[1][i-2],D[1][i-1])
            D[1][i] += max(D[0][i-2],D[0][i-1])
     
    print(max(D[0][n-1],D[1][n-1]))

