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

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
