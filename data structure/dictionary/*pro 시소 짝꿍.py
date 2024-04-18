from collections import Counter
def solution(weights):
    answer = 0
    dic = Counter(weights)
    for k,v in dic.items():
        if v >= 2:
            answer += v*(v-1)//2
    
    weights = set(weights)
    for w in weights:
        if w*(2/3) in weights:
            answer += dic[w*(2/3)] * dic[w]
        if w*(2/4) in weights:
            answer += dic[w*(2/4)] * dic[w]
        if w*(3/4) in weights:
            answer += dic[w*(3/4)] * dic[w]

    return answer