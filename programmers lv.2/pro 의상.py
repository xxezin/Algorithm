def solution(clothes):
    answer = 1
    dic = {}
    for a,b in clothes:
        if b in dic.keys():
            dic[b] += 1
        else:
            dic[b] = 1
    
    for v in dic.values():
        answer *= (v+1)
    
    return answer-1