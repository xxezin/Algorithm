A = input().rstrip()
stack = []
ans = 0
tmp = 1
for i in range(len(A)):
    if A[i] == '(':
        tmp *= 2
        stack.append(A[i])
    
    elif A[i] == '[':
        tmp *= 3
        stack.append(A[i])
    
    elif A[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if A[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
        
    elif A[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if A[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)
