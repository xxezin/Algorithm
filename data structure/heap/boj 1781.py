import sys, heapq
input = sys.stdin.readline

# heapq 이용한건데, 테스트 케이스로 넣어보니까 다른 답이 나옴. 문제 답 자체가 틀린느낌..?
n = int(input())
A = [tuple(map(int,input().split())) for _ in range(n)]
A.sort()

result = 0
heap = []

for i in A:
    heapq.heappush(heap, i[1])
    if i[0] < len(heap): # 날짜보다 개수가 많으면 작은거 pop
        heapq.heappop(heap)

print(sum(heap))


# chk = defaultdict(int)
# for _ in range(n):
#     day, cup = map(int,input().split())
#     if not chk[day] or chk[day] < cup:
#         if day < n:
#             chk[day] = cup

# result = 0
# for v in chk.values():
#     result += v
    
# print(result)