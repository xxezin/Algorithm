import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    tmp = int(input())
    while stack and stack[-1] <= tmp:
        stack.pop()
    stack.append(tmp)
    
print(len(stack))