import sys
input = sys.stdin.readline

n = int(input())
R = [int(input()) for _ in range(n)]

def solution(n, R):
    result= 0
    
    R.sort()
    for i in range(n):
        if R[i]*(n-i) > result:
            result = R[i]*(n-i)
    return result
print(solution(n,R))