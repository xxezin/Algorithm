from collections import deque
import sys
input = sys.stdin.readline

N,L = map(int,input().split())
A = list(map(int,input().split()))
queue = deque()

for i in range(N):
    while queue and queue[-1][0] > A[i]:
        queue.pop()
    while queue and queue[0][1] < i-L+1:
        queue.popleft() #if로 했더니 시간초과나네...
    queue.append((A[i],i))
    print(queue[0][0],end=" ")