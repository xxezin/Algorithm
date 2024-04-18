import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append(list(map(int,input().split())))

D = [0]*(n+1)

for i in range(n-1,-1,-1):
    if i+A[i][0] > n: # 일수를 넘기는 애들에 대해서
        D[i] = D[i+1] # 상담하지 않음
    
    else: # 일수 안에 있는 애들에 대해서
        D[i] = max(D[i+1],A[i][1]+D[i+A[i][0]]) # 

print(D[0])