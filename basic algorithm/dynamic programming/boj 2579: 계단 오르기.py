# # 방법 1 : 2차원 배열로 
# import sys
# input = sys.stdin.readline

# n = int(input())
# S = [0]*(n+1)
# for i in range(1,n+1):
#     S[i] = int(input()) # 계단의 점수 저장
# D = [[0,0,0] for _ in range((n+1))]

# D[1][1] = S[1]
# D[1][2] = 0
# if n > 1 :
#     D[2][1] = S[2]
#     D[2][2] = S[1]+S[2]

#     for k in range(3,n+1):
#         D[k][1] = max(D[k-2][1],D[k-2][2]) + S[k]
#         D[k][2] = D[k-1][1] + S[k]

# print(max(D[n][1],D[n][2]))

# 방법 2 : 1차원 배열로
import sys
input = sys.stdin.readline

n = int(input())
S = [0]*(n+1)
D = [0]*(n+1)

sum = 0

for i in range(1,n+1):
    S[i] = int(input())
    sum += S[i]


if n <= 2:
    print(sum)
else:
    D[1] = S[1]
    D[2] = S[2]
    D[3] = S[3]

    for k in range(4,n):
        D[k] = min(D[k-2],D[k-3]) + S[k]
    
    print(sum-min(D[n-1],D[n-2]))