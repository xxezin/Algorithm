## pseudo code
# N : 명령의 수 입력받기
# for N만큼 : push, pop, size, empty, top 검사
import sys
input = sys.stdin.readline

N = int(input())
myStack = []
for i in range(N):
    c = input()
    if c.startswith('push'):
        temp = int(c[5::])
        myStack.append(temp)

    elif c.startswith('pop'):
        if not myStack:
            print(-1)
        else:
            temp = myStack[-1]
            myStack.pop()
            print(temp)

    elif c.startswith('size'):
        temp = len(myStack)
        print(temp)

    elif c.startswith('empty'):
        if not myStack:
            print(1)
        else:
            print(0)
    elif c.startswith('top'):
        if not myStack:
            print(-1)
        else:
            print(myStack[-1])






# 구현, 자료구조, 스택