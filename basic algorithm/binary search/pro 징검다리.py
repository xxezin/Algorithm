def solution(distance, rocks, n):
    answer = 0
    s = 0
    e = distance
    rocks.sort()
    rocks.append(distance)
    
    while s <= e:
        pre_rock = 0
        del_rock = 0
        mid = (s+e)//2 # 커트라인
        for rock in rocks:
            if rock-pre_rock < mid:
                del_rock += 1
                if del_rock > n:
                    break
            else:
                pre_rock = rock
                
        if del_rock > n:
            e = mid -1
        else:
            s = mid + 1
            answer = mid
            
    return answer