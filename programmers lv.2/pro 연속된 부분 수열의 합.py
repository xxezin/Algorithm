def solution(sequence, k):
    answer = [0,1000001]
    i,j = 0,0
    sum = sequence[0]
    while i<=j and j!=len(sequence):
        if sum < k:
            j += 1
            if j == len(sequence):
                break
            sum += sequence[j]
            
        elif sum > k:
            sum -= sequence[i]
            i += 1
            
        else:
            if j-i < answer[1]-answer[0]:
                answer = [i,j]
                
            j += 1
            if j == len(sequence):
                break
            sum += sequence[j]
            
    
    return answer

solution([1,1,1,2,3,4,5],5)