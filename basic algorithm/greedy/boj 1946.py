import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    A = sorted(list(map(int,input().split())) for _ in range(n))

    answer = 1
    prev = A[0][1]
    
    for i in range(1,n):
        if A[i][1] < prev:
            answer += 1
            prev = A[i][1]

    print(answer)