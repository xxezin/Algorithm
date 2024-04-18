s = input().rstrip()
answer = 0
stack = []

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
        
    else:
        if s[i-1] == "(":
            stack.pop()
            answer += len(stack)
        elif s[i-1] == ")":
            stack.pop()
            answer += 1
        
print(answer)