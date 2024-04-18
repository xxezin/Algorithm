def solution(order):
    answer = 0
    stack = []
    now = 0
    for i in range(1,len(order)+1):
        stack.append(i)
        
        while stack and stack[-1] == order[now]:
            stack.pop()
            answer += 1
            now += 1

    return answer

solution([4, 3, 1, 2, 5])