from collections import deque
def solution(priorities,location):
    answer = 0
    queue = deque([(idx,i) for idx,i in enumerate(priorities)])
    
    answer = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue): # 자기보다 우선순위 높은 애가 있으면 다시 큐에 넣음
            queue.append(cur)
        else: # 없으면 실행
            answer += 1
            if cur[0] == location:
                return answer
            