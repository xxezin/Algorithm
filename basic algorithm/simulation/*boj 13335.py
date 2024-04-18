# 모든 트럭들이 다리를 건너는 최단 시간?
from collections import deque
n,w,L = map(int,input().split())
truck = deque(list(map(int,input().split())))
bridge = deque([0]*w)

weight,time = 0,0 # 현재 다리 위 무게, 시간
while True:
    end = bridge.popleft()
    weight -= end
    
    if truck:
        if weight + truck[0] <= L:
            weight += truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
    time += 1
    
    if not bridge:
        break
    
print(time)