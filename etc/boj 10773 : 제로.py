## pseudo code
# K : 갯수
# myStack : 스택
# for K : 입력받은 값
import sys
input = sys.stdin.readline

K = int(input())
myStack = []
for i in range(K):
    temp = int(input())
    if temp == 0 :
        myStack.pop()
    else :
        myStack.append(temp)

print(sum(myStack))






# 구현, 자료구조, 스택