# 팀워크와 코딩 실력이 적절 = 세 팀원의 코딩 실력 합이 0이 되는 팀
from bisect import bisect_left
def bs(start,end,goal):
    global answer
    
    while start < end:
        tmp = A[start] + A[end]
        if tmp < goal:
            start += 1
        elif tmp == goal:
            if A[start] == A[end]:
                answer += (end-start)
            else:
                idx = bisect_left(A,A[end])
                answer += end+1-idx
            start += 1
        else:
            end -= 1

n = int(input())
A = list(map(int,input().split()))
A.sort()

answer = 0
for i in range(n-2):
    start = i+1
    end = n-1
    goal = -A[i]
    bs(start,end,goal)
print(answer)