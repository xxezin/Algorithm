import sys
while True:
    line = sys.stdin.readline().rstrip()
    stack = []
    flag = 0

    if line == ".":
        break

    for i in line:
        if i == "(" or i == "[" :
            stack.append(i)
        elif i== ")":
            if not stack or stack[-1] == "[":
                print("no")
                flag = 1
                break
            else:
                stack.pop()
        elif i=="]":
            if not stack or stack[-1] == "(":
                print("no")
                flag = 1
                break
            else:
                stack.pop()
    if flag == 0:
        if not stack:
            print("yes")

        else:
            print("no")
