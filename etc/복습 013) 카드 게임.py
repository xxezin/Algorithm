# 카드를 버린다
# 카드를 옮긴다
# -> 양방향 -> 양방향은 큐!

from collections import deque
N = int(input())
q = deque()
for i in range(1,N+1):
    q.append(i)

while len(q)>1:
    q.popleft()
    q.append(q.popleft())

print(q[0])