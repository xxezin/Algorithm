import math
def solution(A, B):
    answer = 0
    gcdA = A[0]
    gcdB = B[0]
    
    for a in A[1:]:
        gcdA = math.gcd(a,gcdA)
    for b in B[1:]:
        gcdB = math.gcd(b,gcdB)
    
    if notdiv(gcdA,B):
        answer = max(answer,gcdA)
    if notdiv(gcdB,A):
        answer = max(answer,gcdB)
        
    return answer

def notdiv(value,arr):
    for a in arr:
        if a % value == 0:
            return False
    return True
                