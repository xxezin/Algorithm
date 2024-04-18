def solution(s):
    answer = 0
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        elif not stack or stack[-1] != s[i]:
            stack.append(s[i])
            
    if not stack:
        answer = 1
        
    return answer