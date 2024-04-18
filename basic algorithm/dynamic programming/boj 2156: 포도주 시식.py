# 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야함.
# 마신 후에는 원래 위치에 다시 놓아햐 함
# 연속으로 놓여있는 3잔을 모두 마실 수는 없음

import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]
D = [[0,0,0] for _ in range(10001)]

# D[i][0] = A[i] 선택하지 않음. 이전거 최대 아무거나 가져와도 됨 = max(D[i-1])
# D[i][1] = A[i] 선택, 이전 거는 선택하지 않음 = D[i-1][0]+A[i]
# D[i][2] = A[i] 선택, 이전 거 선택함 = D[i-1][1] + A[i]

D[0] = [0,A[0],0]
for i in range(1,n):
    D[i][0] = max(D[i-1])
    D[i][1] = D[i-1][0]+A[i]
    D[i][2] = D[i-1][1] + A[i]

print(max(D[n-1]))


# 교훈 : 어떻게 쪼갤 수 있는지에 대해 초점을 맞춰보자.
# 교훈 2 : 테이블을 잘 설정하자