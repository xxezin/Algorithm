from collections import deque

n,w,l = map(int,input().split()) # 트럭 수, 다리 길이, 최대 하중
A = deque(list(map(int,input().split())))

bridge = deque([0]*w)

weight,time = 0,0 # 무게, 시간 
while True:
    now = bridge.popleft()
    weight -= now
    
    if A:
        if weight + A[0] <= l:
            weight += A[0]
            bridge.append(A.popleft())
        else:
            bridge.append(0)
    time += 1
    
    if not bridge:
        break

print(time)