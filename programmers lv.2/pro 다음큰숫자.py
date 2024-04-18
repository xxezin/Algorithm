def solution(n):
    num = len(bin(n)[2:].replace('0',''))
    m = n+1
    big = len(bin(m)[2:].replace('0',''))
    
    while big != num:
        m += 1
        big = len(bin(m)[2:].replace('0',''))
    
    return m

print(solution(15))