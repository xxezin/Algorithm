N = int(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num+=1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su :
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result :
    print(answer)

## 자료구조에 대해 배우면서 파이썬에 대한 이해도가 커지는듯
## 하지만 만들어진 코드 이해도 어렵다... 꾸준히가 답인듯