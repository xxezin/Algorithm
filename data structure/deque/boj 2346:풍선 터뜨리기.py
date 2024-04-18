from collections import deque
n = int(input())
A = deque(map(int,input().split()))

now = A.popleft()
while A:
    for i in range(n):
        if A[i] > 0:
            A.popleft()