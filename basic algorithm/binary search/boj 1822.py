import sys
input = sys.stdin.readline

a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

C = A-B

if C:
    C = sorted(C)
    print(len(C))
    print(' '.join(map(str,C)))
else:
    print(0)