import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
A.sort() # 시작 시간 기준으로 정렬

heap = []
heapq.heappush(heap,A[0][1])

for i in range(1,n):
    if A[i][0] < heap[0]:
        heapq.heappush(heap,A[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,A[i][1])
        
print(len(heap))


# for i in range(1,n):
#     while A[i][0] < now:
#         heapq.heappush(heap,A[i])
#         ans +=1
#         i+=1

#     if heapq:
#         now = heapq.heappop(heap)[1]

