from collections import deque
def solution(n, k):
    answer = 0
    A = deque()
    
    while n > 0:
        a,b = divmod(n,k) # 몫과 나머지
        A.appendleft(b)
        n //= k
        
    tmp = (''.join(map(str,A))).split('0')
    
    def sosu(v):
        import math
        if v==1:
            return 0
        for i in range(2,int(math.sqrt(v))+1):
            if v%i == 0:
                return 0
        return 1
    
    for i in tmp:
        if i=='':
            continue
        if sosu(int(i)):
            answer += 1
    return answer