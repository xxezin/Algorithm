from collections import deque
N = int(input())
queue = deque()

for i in range(1,N+1):
    queue.append(i) # 1부터 N까지

while len(queue) > 1 :
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])