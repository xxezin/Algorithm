import sys
input = sys.stdin.readline

answer = []
num = 1
while True:
    tmp = input().rstrip()
    if tmp[0] == "-":
        break
    
    if tmp == "":
        answer.append((num,0))
        num += 1
        continue
    
    stack = []
    for i in tmp:
        if i == "{":
            stack.append(i)
        else:
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
    if stack:
        change = 0
        for i in range(len(stack)-1,-1,-1):
            if i%2 == 1 and stack[i] == "{":
                change += 1
            elif i%2 == 0 and stack[i] == "}":
                change += 1
        answer.append((num,change))               
            
    else:
        answer.append((num,0))
    num += 1

for i,j in answer:
    print(f'{i}. {j}')