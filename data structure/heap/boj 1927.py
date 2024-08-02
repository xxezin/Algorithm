import sys, heapq
input = sys.stdin.readline

def solution(calc):
    heap = []
    for c in calc:
        if c == 0:
            if not heap:
                print(0)
                continue
            print(heapq.heappop(heap))
            continue
        heapq.heappush(heap, c)


n = int(input())
calc = [int(input()) for _ in range(n)]
solution(calc)