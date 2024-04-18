import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    tmp = input().rstrip()
    stack = []
    flag = False
    for i in tmp:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                flag = True
                print("NO")
                break
            else:
                stack.pop()
    if not flag:
        if stack:
            print("NO")
        else:
            print("YES")