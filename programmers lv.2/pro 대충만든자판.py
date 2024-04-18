def click(t,keymap):
    answer = 0
    for i in t: # t = "ABCD"
        min_v = 100000
        for k in keymap: # keymap = ["ABACD","BCEFD"]
            if k.find(i) >= 0:
                min_v = min(k.find(i),min_v)
        answer += min_v+1
    
    return answer


def solution(keymap, targets):
    answer = []
    for t in targets:
        answer.append(click(t,keymap))
        
    return answer

solution(["ABACD", "BCEFD"],["ABCD","AABB"]	)