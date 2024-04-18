def solution(n, left, right):
    A = []
    for i in range(left,right+1):
        a = i // n
        b = i % n
        if a < b:
            a,b = b,a
        A.append(a+1)
    
    return A