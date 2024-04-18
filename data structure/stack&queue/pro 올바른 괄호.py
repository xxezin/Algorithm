def solution(s:str)->bool:
    answer = True
    S = list(s)
    q = []
    
    for i in range(len(S)):
        if S[i]=='(':
            if not q or q[-1]=='(':
                q.append(S[i])
            elif q[-1]==')':
                answer = False
                break

        elif S[i]==')':
            if q and q[-1]=='(':
                q.pop()
            else:
                answer = False
                break
    if q:
        answer = False
    return answer

solution("(()(")