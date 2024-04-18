def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    
    answer = []
    for i in s:
        i = i.split(',')
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return list(map(int,answer))