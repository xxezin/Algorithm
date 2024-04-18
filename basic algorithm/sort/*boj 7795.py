import sys
input = sys.stdin.readline


# 버전 1. bisect_left 이용
# from bisect import bisect_left

# def bs(A,B):
#     answer = 0
#     for a in A:
#         answer += bisect_left(B,a)
#     return answer
    

# T = int(input())
# for _ in range(T):
#     N,M = map(int,input().split())
#     A = sorted(list(map(int,input().split())))
#     B = sorted(list(map(int,input().split())))

#     print(bs(A,B))

# 버전 2. 이분탐색 구현 - 시간초과로 실패
# def bs(search,data):
#     s,e = 0,len(data)-1
#     res = -1
#     while s <= e:
#         mid = (s+e)//2
#         if data[mid] < search:
#             res = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return res

# T = int(input())
# for _ in range(T):
#     N,M = map(int,input().split())
#     A = sorted(list(map(int,input().split())))
#     B = sorted(list(map(int,input().split())))
    
#     ans = 0
#     for a in A:
#         ans += bs(a,B) +1
#     print(ans)
    
# 버전 3. 비교
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    
    ans = 0
    j = 0
    for i in range(N):
        while j < M:
            if A[i] > B[j]:
                j += 1
            else:
                ans += j
                break
        else:
            ans += M
            
    print(ans)