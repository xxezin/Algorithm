from collections import deque
s = deque(input().rstrip())

answer = ""
tmp = ""
while s:
    if s[0] == "<":
        while s and s[0] != ">":
            answer += s.popleft()
        answer += s.popleft()
    
    elif s[0].isalnum():
        while s and s[0] != ' ' and s[0] != "<":
            tmp += s.popleft()
        answer += tmp[::-1]
        tmp = ""
    
    elif s[0] == ' ':
        answer += s.popleft()
        
print(answer)