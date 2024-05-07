# 스택 두개로 구현해보자
import sys
input = sys.stdin.readline

A = list(input().rstrip()) # 왼쪽 스택
B = list() # 오른쪽 스택
rep = int(input()) # 횟수


for _ in range(rep):
    tmp = list(input().split())
    if tmp[0] == 'L' and A:
        B.append(A.pop())
    elif tmp[0] == 'D' and B:
        A.append(B.pop())
    elif tmp[0] == 'B' and A:
        A.pop()
    elif tmp[0] == 'P':
        A.append(tmp[1])
        
while B:
    A.append(B.pop())
    
print(''.join(A))