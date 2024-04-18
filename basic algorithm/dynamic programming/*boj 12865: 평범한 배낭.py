## 틀린 풀이 ##
# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# A = [list(map(int,input().split())) for _ in range(n)]
# A.sort(key=lambda x:x[0], reverse=True) # 아이템을 무게가 큰 순서대로 정렬

# ans = []
# for i in range(n):
#     tmp = 0
#     mg = k

#     if mg-A[i][0] >=0: # 담을 수 있으면
#         mg-=A[i][0]
#         tmp += A[i][1] # 가치 더해줌

#         for j in range(i+1,n):
#             if mg-A[j][0] >= 0: # 담을 수 있으면
#                 mg-=A[j][0]
#                 tmp += A[j][1]
#             else:
#                 ans.append(tmp)
#                 break   
            
#         ans.append(tmp)
    
#     else: # 담을 수 없으면
#         break

# print(max(ans))

## DP ##
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
A = [[0,0]]
for _ in range(n):
    A.append(list(map(int,input().split())))

D = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w = A[i][0] # 현재 무게
        v = A[i][1] # 현재 가치

        if j < w: # 현재 무게를 담지 못하면
            D[i][j] = D[i-1][j] # 이전 무게를 담은 상태를 유지함
        else: # 담을 수 있다면
            D[i][j] = max(D[i-1][j], D[i-1][j-w]+v) # 이전 물건을 담은 상태와, 현재 물건을 넣었을 때의 가치를 비교해 큰 값을 넣음

print(D[n][k])