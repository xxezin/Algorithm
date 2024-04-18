import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = [int(input()) for _ in range(n)]
A.sort()

# 틀린 풀이
# left, right = 0, n-1
# answer = 10000000000
# while left <= right:
#     if A[right] - A[left] >= m:
#         answer = min(answer, A[right] - A[left])
#         left +=1
#     else:
#         right -=1

# print(answer)

# 맞은 풀이
left, right = 0,0
answer = 10000000000
while right != n:
    if A[right] - A[left] < m:
        right +=1
    elif A[right] - A[left] == m:
        answer = min(answer, A[right] - A[left])
        right +=1
    else:
        answer = min(answer, A[right] - A[left])
        left +=1

print(answer)