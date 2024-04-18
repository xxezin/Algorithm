import sys
input = sys.stdin.readline

D = [0]*(101)
D[1] = 1
D[2] = 1
D[3] = 1

for i in range(4,101):
    D[i] = D[i-2]+D[i-3]

t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    ans.append(D[n])

print('\n'.join(map(str,ans)))