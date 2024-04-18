from collections import deque
def solution(q1, q2):
    answer = 0
    q1 = deque(q1)
    q2 = deque(q2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    tot = sum1+sum2
    
    if tot %2 !=0:
        return -1
    target = tot // 2 # 각 큐의 합이 될 수
    
    while True:
        if sum1 > sum2:
            p = q1.popleft()
            q2.append(p)
            sum1 -= p
            sum2 += p
            answer += 1
            
        elif sum1 < sum2:
            p = q2.popleft()
            q1.append(p)
            sum1 += p
            sum2 -= p
            answer += 1
            
        else:
            break
        if answer == len(q1)*4:
            return -1
    return answer