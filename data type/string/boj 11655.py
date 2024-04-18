S = list(input().rstrip())
for i in range(len(S)):
    if S[i].islower(): # 소문자일때
        if ord(S[i])+13 > 122:
            S[i] = chr(ord(S[i])+13-26)
        else:
            S[i] = chr(ord(S[i])+13)
    elif S[i].isupper(): # 대문자일때
        if ord(S[i])+13 > 90:
            S[i] = chr(ord(S[i])+13-26)
        else:
            S[i] = chr(ord(S[i])+13)

print(''.join(S))
