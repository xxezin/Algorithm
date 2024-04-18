n = int(input())
A = list(map(int,input().split()))

s,e = 0,n-1
ans = A[s]+A[e]

while s < e:
    tmp = A[s]+A[e]
    if tmp==0: # 0 이면 찾은거지
        ans = 0
        break

    if abs(tmp) < abs(ans): # 0에 더 가까우면 업데이트
        ans = tmp
    
    if tmp > 0: # 양수일 때 절댓값 줄이기
        e -= 1
    else: # 음수일 때 절댓값 줄이기
        s += 1
        
print(ans)

# # 틀린 풀이
# n = int(input())
# A = list(map(int,input().split()))

# s,e = 0,n-1
# ans = 200000000
# while s < e:
#     if abs(A[s]+A[e]) <= abs(ans):
#         ans = A[s]+A[e]
#         e -= 1
#     else:
#         s += 1
        
# print(ans)