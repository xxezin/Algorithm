import heapq
def solution(A):
    answer = 0
    for i in range(len(A)):
        for j in range(2):
            A[i][j] = int(A[i][j][:2])*60 + int(A[i][j][3:])
    A.sort(key=lambda x:(x[0],x[1])) # 시작 시간 기준으로, 시작 시간이 같으면 종료 시간 순으로
    
    heap = []
    heapq.heappush(heap,A[0][1])
    
    for i in range(1,len(A)):
        if A[i][0] < heap[0]+10:
            heapq.heappush(heap,A[i][1])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap,A[i][1])

    return len(heap)