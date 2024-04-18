from collections import deque
n,k = map(int,input().split())
A = deque([i for i in range(1,n+1)])

answer = []
while A:
    if len(A) == 1:
        answer.append(A.popleft())
        break
    for _ in range(k-1):
        A.append(A.popleft())
    answer.append(A.popleft())
    
print("<"+', '.join(map(str,answer))+">")