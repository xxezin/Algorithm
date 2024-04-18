import sys
T = int(input())

while True:
    for i in range(T):
        stack = []
        # V_flag = False
        PS = sys.stdin.readline().rstrip()

        for c in PS :
            if c == "(" :
                stack.append(c)
            
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else :
                    stack.append(c)
                
        if not stack :
            print("YES")
        else :
            print("NO")

    break