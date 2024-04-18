n = int(input())
A = list(map(int,input().split()))

stack = []
now = 1
for a in A:
    while stack and stack[-1] <= now:
        stack.pop()
        now += 1
    
    stack.append(a)

if stack:
    while stack:
        if stack.pop() == now:
            now += 1
        else:
            print("Sad")
            break
    else:
        print("Nice")

else:
    print("Nice")