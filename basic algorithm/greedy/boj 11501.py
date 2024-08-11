import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = 0
    n = int(input())
    A = list(map(int,input().split()))
    
    max = 0
    for i in range(len(A)-1,-1,-1):
        if A[i] > max: # max보다 크면 팔만한 주식이 아님. 그리고 얘를 max로
            max = A[i]
        else:
            answer += (max-A[i])
            
    print(answer)