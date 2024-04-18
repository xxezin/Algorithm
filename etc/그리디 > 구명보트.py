from collections import deque
def solution(people, limit):
    count = 0
    people.sort()
    q = deque(people)

    while q:
        if len(q)>=2:
            if q[0]+q[-1] <= limit:
                q.pop()
                q.popleft()
                count+=1
            elif q[0]+q[-1] > limit:
                q.pop()
                count+=1
        else:
            q.pop()
            count+=1
    return count

solution([70,50,80,50,40,60,130,100,40,60],100)