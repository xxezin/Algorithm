A = input()
stack = []
result = 0
stain = 0
# 스택에 인덱스 필요할 너낌...

for i in range(0,len(A)) :
    if A[i] == "(":
        stack.append((i,A[i]))
        stain += 1
    
    if stack[-1][1] == "(" and A[i] == ")":
        if i - stack[-1][0] == 1:
            stain -= 1
            stack.pop()
            result += stain
        else :
            stain -= 1
            result += 1
    
print(result)