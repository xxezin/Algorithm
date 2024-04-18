def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    
    Lost = [l for l in lost if l not in reserve]
    Reserve = [r for r in reserve if r not in lost]
    
    for R in Reserve:
        if R-1 in Lost:
            Lost.remove(R-1)
            
        elif R+1 in Lost:
            Lost.remove(R+1)
    
    return answer-len(Lost)