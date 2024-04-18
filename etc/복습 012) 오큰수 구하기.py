## 핵심 아이디어 ##
# 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수가 된다
# 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력해야 한다

N = int(input())
A = list(map(int,input().split()))
ans = [0]*N
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""

for i in range(N):
    result += str(ans[i])+" "

print(result)