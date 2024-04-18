import sys
input = sys.stdin.readline

n = int(input())
D = [0]*(1001) # 미리 배열의 크기를 최대로 정해놓으면 에러가 나지않음. 왜일까?

D[1] = 1
D[2] = 2
for k in range(3,n+1):
    D[k] = (D[k-1] + D[k-2])%10007

print(D[n])
