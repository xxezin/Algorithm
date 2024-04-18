import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

D = [0]*(n+1)

ans = 0
for i in range(n):
    for j in range(i+A[i][0],n+1): # i번째 날에 상담을 진행했을때, 상담이 가능한 모든 날짜 검사
        D[j] = max(D[j],D[i]+A[i][1]) # j번째 날에 상담 진행했을때를 비교해 최대값 갱신

print(max(D)) # 가장 큰값