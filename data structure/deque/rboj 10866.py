import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
A = deque()

for _ in range(n):
    tmp = list(map(str,input().split()))
    
    if tmp[0] == 'push_front':
        A.appendleft(tmp[1])
        
    elif tmp[0] == 'push_back':
        A.append(tmp[1])
        
    elif tmp[0] == 'pop_front':
        if A:
            print(A.popleft())
        else:
            print(-1)
            
    elif tmp[0] == 'pop_back':
        if A:
            print(A.pop())
        else:
            print(-1)
            
    elif tmp[0] == 'size':
        print(len(A))
        
    elif tmp[0] == 'empty':
        if A:
            print(0)
        else:
            print(1)
    
    elif tmp[0] == 'front':
        if A:
            print(A[0])
        else:
            print(-1)
            
    elif tmp[0] == 'back':
        if A:
            print(A[-1])
        else:
            print(-1)