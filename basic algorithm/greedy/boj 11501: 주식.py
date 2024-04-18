import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))

    result = 0
    max = 0
    for i in range(n-1,-1,-1): # 끝날부터 검사
        if A[i] > max: # max 보다 크다면 업데이트
            max = A[i]
        else:
             result += max-A[i]
    
    print(result)

