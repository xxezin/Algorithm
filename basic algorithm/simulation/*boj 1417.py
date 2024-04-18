# 다솜이가 매수해야하는 사람의 최솟값? -> heap ...
# 다솜이는 기호 1번임
import heapq

n = int(input())
heap = []

for i in range(n):
    v = int(input())
    if i == 0:
        dasom = v
        continue
    
    heapq.heappush(heap,-v)
    
answer = 0
while heap:
    v = -heapq.heappop(heap) 
    if v < dasom: # 최대값이 다솜보다 적으면
        break
    
    dasom += 1
    answer += 1
    heapq.heappush(heap,-(v-1))
    
print(answer)