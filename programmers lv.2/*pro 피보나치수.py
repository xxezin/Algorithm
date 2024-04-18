# 1. 재귀로 구현. 시간 초과로 실패
# def solution(n):

#     def fibo(n):
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             return (fibo(n-1)+fibo(n-2) % 1234567)
        
#     return fibo(n)

# 2. for문으로 구현. 성공
def solution(n):
    answer = []
    for i in range(n+1):
        if i==0:
            answer.append(0)
        elif i==1:
            answer.append(1)
        else:
            answer.append(answer[i-1]+answer[i-2])
    
    return answer[n]%1234567
print(solution(5))