A = list(input())
answer = ''
stack = []

for i in A:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/': # 나눗셈이나 곱셈인 경우 스택에 있는 애들 먼저 처리
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-': # 덧셈이나 뺄셈의 경우 ()안에 있는 것을 제외한 스택에 있는 애들 먼저 처리
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
            
while stack:
    answer += stack.pop()
    
print(answer)