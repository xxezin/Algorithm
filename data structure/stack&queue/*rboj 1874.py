import sys
input = sys.stdin.readline

n = int(input())
A= []
for i in range(n):
    A.append(int(input()))
stack = []

result = True
answer = ""

num = 1
for i in range(n):
    tmp = A[i]
    if tmp >= num:
        while tmp >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > tmp:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)