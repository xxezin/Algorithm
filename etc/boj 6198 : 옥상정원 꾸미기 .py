## pseudo code
# N : 빌딩 갯수
# H : 빌딩 높이 리스트
# stack : [] 준비
# answer : 벤치마킹 가능한 빌딩 수(output)

# for N : 빌딩 갯수만큼 돌면서
#     while stack이 존재하고, 현재 빌딩보다 높은 수들은 pop
#         stack.pop()
#     if stack이 존재하면:
#         answer +=1
#     stack.append([A[i], i+1])
import sys
input = sys.stdin.readline
        
N = int(input())
H = [0]*(N)
stack = []
answer = 0

for i in range(N):
    H[i] = int(input())

for i in range(N):
    while stack and stack[-1][0] <= H[i]:
        stack.pop()
    stack.append([H[i],i+1])

    answer += len(stack)-1

print(answer)