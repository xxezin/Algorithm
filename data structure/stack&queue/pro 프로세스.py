from queue import PriorityQueue

def solution(priorities:list, location:int) -> int:
    answer = 0
    
    
    for idx,p in enumerate(priorities):
        pq.put([p,idx])
    
    return answer

solution([1,1,9,1,1,1],0)