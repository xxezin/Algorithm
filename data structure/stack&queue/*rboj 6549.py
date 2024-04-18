import sys
input = sys.stdin.readline

while True:
    A = list(map(int,input().split()))
    if A == [0]:
        break
    
    n = A[0]
    stack = []
    answer = 0
    
    for i in range(1,n+1):
        idx = i
        while stack and stack[-1][0] >= A[i]:
            answer = max(answer, (i-stack[-1][1])*stack[-1][0])
            idx = stack[-1][1]
            stack.pop()
        
        stack.append([A[i],idx])
    
    while stack:
        answer = max(answer,(n+1-stack[-1][1])*stack[-1][0])
        stack.pop()
    
    print(f'{answer}')