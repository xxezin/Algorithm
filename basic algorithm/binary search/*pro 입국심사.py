def solution(n, times):
    answer = 0
    min_time, max_time = 1, max(times)*n
    while min_time <= max_time:
        mid = (min_time + max_time)//2
        people = 0
        for time in times:
            people += mid//time
            if people >= n:
                break
            
        if people >= n:
            answer = mid
            max_time = mid -1
            
        else:
            min_time = mid +1
    
    return answer