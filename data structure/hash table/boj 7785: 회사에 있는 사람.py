import sys
input = sys.stdin.readline

n = int(input())
A = dict()
for _ in range(n):
    name, log = map(str,input().split())
    if log == "enter":
        A[name] = 1
    else:
        del A[name]

print('\n'.join(sorted(A.keys(),reverse=True)))
