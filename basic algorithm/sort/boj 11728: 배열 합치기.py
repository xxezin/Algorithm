# # 방법 1 : 투포인터 이용
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# ans = [0]*(n+m)

# Aidx, Bidx = 0,0
# for i in range(n+m):
#     if Bidx == m:
#         ans[i] = A[Aidx]
#         Aidx +=1
#     elif Aidx == n:
#         ans[i] = B[Bidx]
#         Bidx +=1
#     elif A[Aidx] <= B[Bidx]:
#         ans[i] = A[Aidx]
#         Aidx +=1
#     else:
#         ans[i] = B[Bidx]
#         Bidx +=1

# print(' '.join(map(str,ans)))
# print(*ans) # 얘가 더 시간을 많이 잡아먹네

# 방법 2: 정렬 이용
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = A+B
ans.sort()

print(*ans)