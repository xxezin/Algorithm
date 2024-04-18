import sys

N = int(input())
result = 0
for i in range(N):
    stack = []
    word = sys.stdin.readline().rstrip()
    k = len(word)

    for c in word:
        pop_flag = False
        while stack and stack[-1]== c:
            stack.pop()
            pop_flag = True

        if pop_flag == False:
            stack.append(c)

    if not stack :
        result +=1

print(result)