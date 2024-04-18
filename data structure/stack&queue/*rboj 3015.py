import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

answer = 0
stack = []
for i in range(n):
    while stack and stack[-1][0] < A[i]: 
        answer += stack.pop()[1]
    
    if not stack:
        stack.append([A[i],1])
        continue
    
    if stack and stack[-1][0] == A[i]: # 스택 끝값 키와 같을때
        cnt = stack.pop()[1]
        answer += cnt
        
        if stack:
            answer += 1
        
        stack.append([A[i],cnt+1])
        
    else: # 스택 끝값 키보다 작을 때
        stack.append([A[i],1])
        answer += 1

print(answer)