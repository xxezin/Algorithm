def solution(p, limit):
    answer = 0
    p.sort()
    a,b = 0,len(p)-1
    while a<b:
        if p[a] + p[b] <= limit: # 같이 탈 수 있으면
            a += 1
            answer += 1 # 같이 탄사람들
        b -= 1
    return len(p) - answer