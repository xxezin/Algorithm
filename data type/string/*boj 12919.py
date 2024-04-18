from collections import deque

s = input().rstrip()
t = deque([input().rstrip()])
while t:
    x = t.popleft()
    if x == s:
        print(1)
        exit()
    elif len(x) < len(s):
        break
        
    if x[-1] == 'A':
        t.append(x[:-1])

    if x[0] == 'B':
        t.append(x[1:][::-1])

print(0)

