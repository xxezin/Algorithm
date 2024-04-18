import sys
input = sys.stdin.readline

n = int(input()) # 학생 수
A = list(str(input().rstrip()) for _ in range(n))

s = len(A[0]) # 문자열 길이
for j in range(s):
    set_num = set()
    for i in range(n):
        set_num.add(A[i][-(j+1):])
    
    if n == len(set_num):
        print(j+1)
        break