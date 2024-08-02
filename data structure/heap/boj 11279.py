import sys, heapq
input = sys.stdin.readline

def solution(A):
    heap = []
    for i in A:
        if i == 0:
            if not heap:
                print(0)
                continue
            print(-heapq.heappop(heap))
            continue
        heapq.heappush(heap, i)

n = int(input())
A = [-int(input()) for _ in range(n)]
solution(A)