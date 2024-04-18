import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
B = sorted(set(A))

# 1. 이진 탐색 구현 - 7332ms
# for i in A:
#     s,e = 0,len(B)-1
#     while s <= e:
#         mid = (s+e)//2
#         if i == B[mid]:
#             print(mid,end=' ')
#             break
#         else:
#             if i < B[mid]:
#                 e = mid-1
#             else:
#                 s = mid+1

# 2. bisect 모듈 - 2656ms
from bisect import bisect_left
for i in A:
    print(bisect_left(B,i),end=' ')