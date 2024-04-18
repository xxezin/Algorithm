# # dfs - 재귀
# from collections import defaultdict
# def solution(tickets):
#     airport = defaultdict(list)
#     for dep,arr in tickets:
#         airport[dep].append(arr)
#     for dep in airport.keys():
#         airport[dep].sort()
        
#     def dfs(path,n):
#         if len(path) == n:
#             return path
#         for idx,i in enumerate(airport[path[-1]]):
#             airport[path[-1]].pop(idx)
#             answer = dfs(path+[i],n)
#             airport[path[-1]].insert(idx,i)
#             if answer:
#                 return answer
            
#     return dfs(['ICN'],len(tickets)+1)


# dfs - 스택
from collections import *
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)
        graph[a].sort(reverse=True)   

    def DFS(now):
        stack = ["ICN"]
        while stack:
            start = stack[-1]
            if not graph[start]:
                answer.append(stack.pop())
            else:
                stack.append(graph[start].pop())

    DFS('ICN')
    return answer[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
    