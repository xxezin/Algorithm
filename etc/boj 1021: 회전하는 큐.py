from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
position = list(map(int,input().split()))
deque = deque([i for i in range(1,N+1)])

count = 0
for i in position:
    while True:
        if deque[0] == i:
            deque.popleft()
            break
        else:
            if deque.index(i) < len(deque)/2:
                while deque[0] != i:
                    deque.append(deque.popleft())
                    count+=1
            else:
                while deque[0] != i:
                    deque.appendleft(deque.pop())
                    count+=1
print(count)




# #왼쪽 이동
# queue.append(queue.popleft())
# #오른쪽 이동
# queue.appendleft(queue.pop())
# #pop(첫번째 원소를 뽑아내니깐)
# queue.popleft()

