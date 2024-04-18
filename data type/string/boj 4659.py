import sys
input = sys.stdin.readline

a = {"a","e","i","o","u"}
while True:
    tmp = input().rstrip()
    if tmp=='end':
        break
    
    v,nv = 0,0
    flag,answer = False,True
    stack = []
    
    for i in tmp:
        if i in a:
            flag = True
            v += 1
            nv = 0
        else:
            nv += 1
            v = 0
        
        if v == 3 or nv == 3:
            answer = False
            break
        
        if stack:
            if stack[-1] == i:
                if i == 'e' or i == 'o':
                    continue
                answer = False
                break
            stack.append(i)
        else:
            stack.append(i)
    
    if answer and flag:
        print(f"<{tmp}> is acceptable.")
    else:
        print(f"<{tmp}> is not acceptable.")