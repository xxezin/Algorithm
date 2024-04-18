# 스택 활용
# def solution(s):
#     stack = []
#     answer = True
#     for i in s:
#         if i == '(':
#             stack.append(i)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 answer = False
#                 break
#     if stack:
#         answer = False
#     return answer


# 큐 활용
from collections import deque
def solution(s):
    q = deque()
    answer = True
    for i in s:
        if i == '(':
            if not q or q[-1] != ')':
                q.append(i)
            else:
                answer = False
                break
            
        else:
            if q and q[-1] =='(':
                q.pop()
            else:
                answer = False
                break
            
    if q:
        answer = False
    return answer

    
print(solution("()()"))
print(solution(")()("))