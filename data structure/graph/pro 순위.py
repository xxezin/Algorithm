def solution(n, results):
    answer = 0
    A = [[] for _ in range(n+1)]
    for i,j in results:
        A[i].append([j,-1]) # 진 쪽
        A[j].append([i,1]) # 이긴 쪽
    
    lst = []
    for i in range(1,n+1):
        if len(A[i]) == n-1:
            answer += 1
            lst.append(i)
            for j in A[i]:
                if j[1] == -1 and j not in lst:
                    answer += 1
                    lst.append(j[0])
                 
    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])