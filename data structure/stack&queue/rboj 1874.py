import sys
input = sys.stdin.readline

n = int(input())
A = list(int(input()) for _ in range(n))

answer = []
stack = []
num = 0

for a in A:
    while not stack or (stack and stack[-1] < a):
        num += 1
        stack.append(num)
        answer.append("+")
    
    if stack and stack[-1] == a:
        stack.pop()
        answer.append("-")
    elif stack and stack[-1] != a:
        print("NO")
        exit()

print('\n'.join(answer))