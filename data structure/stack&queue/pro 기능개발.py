# def solution(progresses:list, speeds:list) -> list:
#     answer = []
#     task = []

#     for idx,p in enumerate(progresses): # 해당 작업이 소요되는 기간을 task에 담음
#         tmp = divmod((100-p),speeds[idx])
#         if tmp[1] > 0:
#             task.append(tmp[0]+1)
#         elif tmp[1] == 0:
#             task.append(tmp[0])

#     ans = 1
#     q = []
#     for t in task:
#         while q:
#             if t <= q[0]:
#                 ans += 1
#                 break
#             elif t > q[0]:
#                 q = []
#                 answer.append(ans)
#                 ans = 1
            
#         q.append(t)
    
#     if q:
#         answer.append(ans)
        
#     return answer

## 참고할만한 풀이
def solution(progresses:list, speeds:list) -> list:
    q = []
    for p,s in zip(progresses,speeds):
        if not len(q) or q[-1][0] < -((p-100)//s):
            q.append([-((p-100)//s),1])
        else:
            q[-1][1] +=1
    
    return [Q[1] for Q in q]

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))