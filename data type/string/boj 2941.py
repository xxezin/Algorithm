s = input().rstrip()
answer = 0

i = len(s)-1 # 포인터
while i > 0:
    if s[i] == '=':
        if s[i-1] in {'s','c'}:
            answer += 1
            i -= 2
        elif s[i-1] == 'z':
            if i-1 > 0 and s[i-2] == 'd':
                answer += 1
                i -= 3
            else:
                answer += 1
                i -= 2
    
    elif s[i] == '-':
        if s[i-1] in {'c','d'}:
            answer += 1
            i -= 2
    
    elif s[i] == 'j':
        if s[i-1] in {'l','n'}:
            answer += 1
            i -= 2
    
    else:
        answer += 1
        i -= 1
            
print(answer)