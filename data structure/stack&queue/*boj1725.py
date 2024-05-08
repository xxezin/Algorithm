import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0

for i in range(N):
    nowV = int(input())
    start = i
    while stack and stack[-1][1] >= nowV: # 현재 값과 같거나 큰 값이 스택에 있으면
        start, preV = stack.pop() # 빼서 직사각형의 넓이를 구함
        result = max(result, (i-start)*preV) # 크다면 업데이트
    stack.append([start,nowV])
    
while stack:
    start, preV = stack.pop()
    result = max(result, (N-start)*preV)

print(result)