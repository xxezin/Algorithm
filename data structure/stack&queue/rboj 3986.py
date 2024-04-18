import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    tmp = input().rstrip()
    
    stack = []
    for i in tmp:
        if stack and stack[-1] == i:
            stack.pop()
        elif not stack or stack[-1] != i:
            stack.append(i)
        
    if not stack:
        cnt += 1
        
print(cnt)