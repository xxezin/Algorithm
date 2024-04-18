import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # 수의 개수, 합을 구해야 하는 횟수
A = list(map(int,input().split()))
ans = []

D = [0]*(1000001)

for i in range(1,n+1):
    D[i] = D[i-1] + A[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    ans.append(D[j]-D[i-1])

print('\n'.join(map(str,ans)))