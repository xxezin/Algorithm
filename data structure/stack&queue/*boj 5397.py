t = int(input())
for _ in range(t):
    s = input().rstrip()
    left,right = [],[]
    
    for idx,i in enumerate(s):
        if i == "-":
            if left:
                left.pop()
        elif i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        else:
            left.append(i)
            
    print(''.join(left) + ''.join(right[::-1]))