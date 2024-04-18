def solution(n):
    A = []

    while n > 0:
        tmp = n % 3
        if not tmp: # 3으로 나눠지는 숫자면
            tmp = 4
            n -= 1
        A.append(str(tmp))
        n //= 3
        
    return ''.join(A[::-1])