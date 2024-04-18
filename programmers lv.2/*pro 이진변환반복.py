def solution(s):
    change = 0
    zero = 0
    
    while int(s) > 1:
        zero += s.count('0')
        s = s.replace('0','')
        
        s = bin(len(s))[2:]
        change += 1
        print(s)
    return [change, zero]

solution("110010101001")