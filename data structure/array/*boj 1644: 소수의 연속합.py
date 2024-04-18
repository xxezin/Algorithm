import math
n = int(input())

# n 이하면서 소수인 리스트
A = [i for i in range(n+1)]
A[1] = 0
for i in range(2, int(math.sqrt(n+1))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        A[j] = 0

# 소수들의 누적합 리스트
B = [0]
sum = 0
for i in range(2,n+1):
    if A[i]:
        sum += A[i]
        B.append(sum)
print(B)
left,right,cnt = 0,1,0

while right < len(B):
    tmp = B[right]- B[left]
    if tmp == n:
        cnt += 1
        left += 1

    elif tmp > n:
        left += 1
    
    else:
        right += 1

print(cnt)

# left,right = 2,2
# cnt = 0
# sum = A[left]

# while right < n:
#     if sum < n:
#         right +=1
#         if A[right] != 0:
#             sum += A[right]
#         elif A[right] == 0:
#             while A[right] == 0 and right < n:
#                 right += 1
#             sum += A[right]

#     elif sum > n:
#         sum -= A[left]
#         left += 1
#         if A[left] != 0:
#             continue
#         else:
#             while A[left] == 0 and left < right:
#                 left +=1
      
#     else:
#         cnt += 1
#         right += 1
#         if A[right] != 0:
#             sum += A[right]
#         else:
#             while A[right] == 0 and right < n:
#                 right += 1
#             sum += A[right]

# if A[n] != 0:
#     print(cnt+1)
# else:
#     print(cnt)