def solution(storey):
    answer = 0

    while storey > 0:
        remain = storey % 10
        if remain > 5:
            storey += (10-remain)
            answer += (10-remain)
            
        elif remain < 5:
            storey -= remain
            answer += remain
            
        else:
            if (storey//10) % 10 > 4:
                storey += 10
            answer += remain
        storey //= 10
        
    return answer

solution(1)
solution(6)