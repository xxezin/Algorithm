# 합을 나타낼 수 있는 경우의 수. 수를 1개 이상 사용해야 함.

# 1 = 1 =1가지
# 2 = 1+1, 2 =2가지
# 3 = 1+1+1, 1+2, 2+1, 3 =4가지
# 4 = 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 =7가지
# 5 = 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 3+1+1, 1+3+1, 1+1+3
#     1+2+2, 2+1+2, 2+2+1, 2+3, 3+2,

import sys
input = sys.stdin.readline

D = [0]*(1000001)
D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4,1000001):
    D[i] = (D[i-1]+D[i-2]+D[i-3])%1000000009

t = int(input())
ans = []
for _ in range(t):
    tmp = int(input())
    ans.append(D[tmp])

print('\n'.join(map(str,ans)))
