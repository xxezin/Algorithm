from collections import deque
def solution(prices):
    answer = []
    
    prices = deque(prices)
    while prices:
        cnt = 0
        now = prices.popleft()
        for k in prices:
            cnt += 1
            if now > k: # 가격이 떨어지면
                break
        answer.append(cnt)
       
    return answer

print(solution([1, 2, 3, 2, 3]))