import sys
input = sys.stdin.readline

A = list(input())[:-1]
B = []
n = int(input())
for _ in range(n):
    tmp = list(input().split())
    if A and tmp[0]=='L':
        B.append(A.pop())
    elif tmp[0] == 'P':
        A.append(tmp[1])
    elif A and tmp[0] == 'B':
        A.pop()
    elif B and tmp[0] == 'D':
        A.append(B.pop())

while B:
    A.append(B.pop())

print(''.join(A))