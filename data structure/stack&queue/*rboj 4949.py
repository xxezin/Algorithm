import sys
input = sys.stdin.readline

while True:
    tmp = input().rstrip()
    if tmp == '.':
        break
    
    stack = []
    flag = True
    for i in tmp:
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')':
            if not stack or stack[-1] == '[':
                flag = False
                print('no')
                break
            else:
                stack.pop()
        
        elif i == ']':
            if not stack or stack[-1] == '(':
                flag = False
                print('no')
                break
            else:
                stack.pop()
            
    
    if flag:
        if not stack:
            print('yes')
        else:
            print('no')