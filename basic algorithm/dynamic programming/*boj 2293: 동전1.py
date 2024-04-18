import sys
input = sys.stdin.readline

n,k = map(int,input().split())
A = [int(input()) for _ in range(n)]

D = [0 for _ in range(k+1)]
D[0] = 1

for i in A: # 코인의 종류별로 돌아가면서
    for j in range(i,k+1): # 가치 i인 코인은 i번째부터 등장 가능
        D[j] += D[j-i]

print(D[k])