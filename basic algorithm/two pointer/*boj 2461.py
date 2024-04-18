import sys
from collections import deque
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())
students = [deque(sorted(list(map(int,input().split())))) for _ in range(n)]

heap = []

min_v = int(10e9)
max_v = 0

for i in range(len(students)): # 각 학급의 최소값만 넣어서 갱신
    v = students[i].popleft()
    max_v = max(max_v,v)
    min_v = min(min_v,v)
    heapq.heappush(heap,[v,i]) # 숫자와 몇번째 그룹에 속하는지. 최소힙

sumation = max_v - min_v

while heap:
    prev_min_v, pos = heapq.heappop(heap) # 최소힙에서 최소값과 그 학급 pop
    if not students[pos]: # 해당 학급에 학생이 남아있지 않으면 
        break
    
    new_v = students[pos].popleft()
    heapq.heappush(heap,[new_v,pos])
    
    if max_v < new_v:
        max_v = new_v
    min_v = heap[0][0]
    sumation = min(sumation,max_v-min_v)
    
print(sumation)