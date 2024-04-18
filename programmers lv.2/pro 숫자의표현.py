def solution(n):
    answer = 0
    A = [i for i in range(n+1)]
    
    i,j =0,0
    while j<=n:
        tmp = sum(A[i:j+1])
        if tmp == n:
            answer += 1
            j += 1
        elif tmp < n:
            j += 1
        elif tmp > n:
            i += 1
            
    return answer

solution(15)