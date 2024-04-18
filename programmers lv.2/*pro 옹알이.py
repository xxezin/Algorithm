def solution(babbling):
    answer = 0
    pro = ["aya","ye","woo","ma"]
    
    for bab in babbling:
        for p in pro:
            if p*2 not in bab:
                bab = bab.replace(p," ")

        if bab.isspace():
            answer += 1
    return answer

solution(["aya", "yee", "u", "maa"])