n = int(input())
A = list(map(int,input().split()))
stack = []

for i in range(n):
    while stack and stack[-1][0] < A[i]:
        stack.pop()
    if stack:
        print(stack[-1][1],end=' ')
    else:
        print(0,end=' ')
    
    stack.append([A[i],i+1])