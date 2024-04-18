import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int,input().split()))
A.sort() # 재배열 가능

B = list(map(int,input().split()))
B.sort(reverse=True) # 생각해보면 A 배열을 바꿀 수 있으니 얘를 바꿔도 댐

S = 0

for i in range(n):
    S += A[i]*B[i]

print(S)