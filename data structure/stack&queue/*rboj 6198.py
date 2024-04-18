# 관리인이 볼 수 있는 다른 빌딩의 옥상 정원 수의 합
import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
    
stack = []
answer = 0
for i in range(n):
    while stack and stack[-1][0] <= A[i]:
        stack.pop()
    stack.append([A[i],i+1])
    
    answer += len(stack)-1
    
print(answer)