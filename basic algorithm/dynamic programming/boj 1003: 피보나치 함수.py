import sys
input = sys.stdin.readline

t = int(input())
D = [[0,0] for _ in range(41)]
D[0][0], D[0][1] = 1,0
D[1][0], D[1][1] = 0,1

for k in range(2,41):
    D[k][0] = D[k-1][0] + D[k-2][0]
    D[k][1] = D[k-1][1] + D[k-2][1]

for _ in range(t):
    tmp = int(input())
    print('{0} {1}'.format(D[tmp][0],D[tmp][1]))