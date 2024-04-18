import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    a,b = map(str,input().split())

    a = dict(a)
    b = dict(b)

    res = "Possible"
    for i in a:
        if i in b:
            
        else:
            res = "Impossible"

    result.append(res)

print('\n'.join(result))
    