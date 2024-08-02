import sys, heapq
input = sys.stdin.readline

def solution(A):
    cnt = 0
    heapq.heapify(A)
    while A:
        if len(A) == 1:
            break
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        heapq.heappush(A, a+b)
        cnt += (a+b)
    
    return cnt


n = int(input())
A = [int(input()) for _ in range(n)]
print(solution(A))