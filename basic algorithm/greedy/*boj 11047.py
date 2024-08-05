import sys
input = sys.stdin.readline

n,k = map(int,input().split())
A = [int(input()) for _ in range(n)]

def solution(n,k,A):
    A.sort(reverse=True)
    cnt = 0
    for a in A:
        if k == 0:
            return cnt
        div, mod = divmod(k,a)
        cnt += div
        k = mod
    return cnt
print(solution(n,k,A))