A = input().rstrip()
stack = []
ans = 0
for idx,i in enumerate(A):
    if i == '(':
        stack.append((i,idx))
    
    else:
        if stack[-1][1] == idx-1: # 레이저인 경우
            stack.pop()
            ans += len(stack)
        else: # 쇠막대기인 경우
            stack.pop()
            ans += 1
            
print(ans)