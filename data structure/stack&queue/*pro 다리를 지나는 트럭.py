from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    nowWeight = 0
    truck_weights = deque(truck_weights)
    q = deque([0]*bridge_length)
    
    while q: # 시간이 흐르는 걸 기반으로
        time += 1
        if q[0] != 0: # 다리를 다 건너 나갈 트럭이 있음 빼줌
            nowWeight -= q[0]
        q.popleft()
        
        if truck_weights: # 다리를 건널 트럭이 있으면
            if nowWeight + truck_weights[0] <= weight:
                nowWeight += truck_weights[0]
                q.append(truck_weights.popleft())
            else:
                q.append(0)
                
    return time