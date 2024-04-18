def solution(L, x):
    for i in range(len(L)):
        if L[i] > x:
            L.insert(i,x)
            break
    if L[0] > x:
        L.insert(0, x)
    if L[-1] < x:
        L.append(x)
    answer = L
    return answer

solution([20,37,58,72,91],65)