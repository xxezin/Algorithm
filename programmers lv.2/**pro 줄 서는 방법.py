import math
def solution(n, k):
    answer = []
    num = [i for i in range(1,n+1)]
    k -= 1
    
    while num:
        a = k//math.factorial(n-1)
        answer.append(num[a])
        del num[a]
        
        k = k % math.factorial(n-1)
        n -= 1
    return answer