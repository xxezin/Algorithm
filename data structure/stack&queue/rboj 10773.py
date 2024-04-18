import sys
input = sys.stdin.readline

k = int(input())
stack = []
for i in range(k):
    tmp = int(input())
    if tmp != 0:
        stack.append(tmp)
    else:
        stack.pop()

print(sum(stack))