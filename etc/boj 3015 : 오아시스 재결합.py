import sys
input = sys.stdin.readline

N = int(input())
A = [0]*N
stack = [] # height, cnt
result = 0

for i in range(N):
    A[i] = int(input())

for i in range(N):
    while stack and stack[-1][0] < A[i]:
        result += stack[-1][1]
        stack.pop()
    if not stack:
        stack.append([A[i],1])
        continue # for문의 다음으로
    if stack[-1][0]!=A[i]:
        result +=1
        stack.append([A[i],1])
    else:
        result += stack[-1][1]
        if len(stack) != 1:
            result +=1
        stack[-1][1] +=1

print(result)