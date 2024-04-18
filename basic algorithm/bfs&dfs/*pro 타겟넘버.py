# # dfs 이용
# def dfs(numbers,target,depth):
#     answer = 0
#     if depth == len(numbers):
#         if sum(numbers) == target:
#             return 1
#         else:
#             return 0
    
#     else:
#         answer += dfs(numbers, target, depth+1)
#         numbers[depth] *= -1
#         answer += dfs(numbers, target, depth+1)
#         return answer

# def solution(numbers, target):
#     answer = dfs(numbers, target,0)
#     return answer

# # bfs 이용
# from collections import deque
# def solution(numbers, target):
#     answer = 0
    
#     q = deque()
#     q.append([numbers[0],0])
#     q.append([-numbers[0],0])
#     while q:
#         tmp,idx = q.popleft()
#         idx += 1
#         if idx < len(numbers):
#             q.append([tmp+numbers[idx],idx])
#             q.append([tmp-numbers[idx],idx])
#         else:
#             if tmp == target:
#                 answer += 1
#     return answer

print(solution([1,1,1,1,1],3))