# T초 동안 자두가 떨어짐(1<=T<=1000)
# 매 초마다 어느 나무에서 자두가 떨어질지에 대한 정보가 나타남
# 자두가 받을 수 있는 자두의 개수?
# 자두는 최대 W 이내만 움직이고 싶음(1<=W<=30)
# 자두의 초기 위치 : 1번 나무

import sys
input = sys.stdin.readline

t,w = map(int,input().split())
A = [0]
for _ in range(t):
    A.append(int(input()))

D = [[0]*(w+1) for _ in range(t+1)]

for i in range(1,t+1):
    # 1번 나무에서 가만히 있는 경우, 1번 나무에서 자두가 떨어지면
    if A[i]== 1:
        D[i][0] = D[i-1][0] +1
    else: # 2번 나무에서 자두가 떨어지면
        D[i][0] = D[i-1][0]
    
    # 움직이면
    for j in range(1,w+1):
        if A[i]==2 and j%2==1: # i초에 2번 나무에서 자두 떨어짐. 현재 2번 나무에 있음
            D[i][j] = max(D[i-1][j-1], D[i-1][j]) +1
        elif A[i]==1 and j%2==0:
            D[i][j] = max(D[i-1][j-1], D[i-1][j]) +1
        else: # 못 먹는 경우
            D[i][j] = max(D[i-1][j-1], D[i-1][j])

print(max(D[t]))



# D[1] # 안움직이면 =0, 움직이면 =1
# D[2] # 이전에 안움직였으면 =1, 이전에 움직였는데 또 움직이면 2

# 안움직였을때 받는 수
# 움직였을때 받는 수

# 움직임이 최소...
# length를 저장하면 되나? ... length 와 idx?