import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in tmp:
        if len(pq) < n: # 힙 길이를 n 이하로 유지
            heapq.heappush(pq,i)
        else:
            if pq[0] < i: # 힙의 최소보다 크면 넣기
                heapq.heappop(pq)
                heapq.heappush(pq,i)

print(pq[0]) # 최댓값만을 넣은 최소힙이니 맨 앞수가 n번째 큰수