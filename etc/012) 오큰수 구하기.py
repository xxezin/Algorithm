N = int(input()) # 수열의 개수
ans = [0]*N # 정답 리스트
A = list(map(int,input().split())) # 수열 리스트 채우기
myStack = [] # 스택 선언

for i in range(N):
    while myStack and A[myStack[-1]] < A[i] :
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack : # 반복문을 다 돌고 나왔는데 스택이 안비어있으면 빌때까지(오큰수가 없었단 소리)
    ans[myStack.pop()] = -1

result = ""
for i in range(N):
    result += str(ans[i])+" "

print(result)
