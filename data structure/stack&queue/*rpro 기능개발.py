from collections import deque
def solution(progresses,speeds):
    days = []
    for pair in zip(progresses,speeds):
        tmp = (100-pair[0])/pair[1]
        if int(tmp) != tmp:
            days.append(int(tmp)+1)
        else:
            days.append(int(tmp))
    
    answer = []
    cnt = 1
    q = deque()
    for i in days:
        while q:
            if i <= q[0]: # 배포의 첫번째 프로세스보다 적게 걸리면 일단 보류
                cnt += 1
                break
            
            else:
                q = deque() # 배포의 첫번째 프로세스보다 오래걸리면 배포 후 다음 배포로
                answer.append(cnt)
                cnt = 1
        q.append(i)
    
    if q: # 남은 프로세스 배포
        answer.append(cnt)           
        
    return answer
        
print(solution([93,30,55],[1,30,5]))
print(solution([95,90,99,99,80,99],[1,1,1,1,1,1]))