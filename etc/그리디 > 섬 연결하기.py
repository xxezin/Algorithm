import heapq


def solution(n, costs):
    answer = 0

    costs_all = [[] for _ in range(n)]

    visited = [False] * n

    heap = []
    heapq.heappush(heap, [0, 0])

    for cost in costs:
        s, e, w = cost
        costs_all[s].append([w, e])
        costs_all[e].append([w, s])

    cnt = 0

    while cnt < n:
        w, s = heapq.heappop(heap)
        if visited[s]:
            continue

        visited[s] = True
        answer += w
        cnt += 1
        for cost in costs_all[s]:
            heapq.heappush(heap, cost)

    return answer

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])

[[[1, 1], [2, 2]], [[1, 0], [5, 2], [1, 3]], [[2, 0], [5, 1], [8, 3]], [[1, 1], [8, 2]]]