import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    A = list(map(int,input().split())) # 학생의 선호 리스트
    
    visited = [False]*n # 방문 리스트
    cycle = [False]*n # 사이클

    for j in range(n):
        if visited[j]:
            continue

        visited[j] = True
        cur = j
        order = [cur]

        while True:
            next = A[cur]-1
            if visited[next]:
                if next not in order:
                    break
            else:
                j = order.index(next)
                for k in range(j,len(order)):
                    cycle[order[k]] = True
                break

            visited[next] = True
            order.append(next)
            cur = next

    print(n-sum(cycle))
