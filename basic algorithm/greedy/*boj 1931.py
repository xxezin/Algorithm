import sys
input = sys.stdin.readline

n = int(input())
T = [tuple(map(int,input().split())) for _ in range(n)]

def solution(n,T):
    cnt = 0
    
    now = 0
    T.sort(key=lambda x:(x[1],x[0]))
    for s,e in T:
        if now <= s:
            cnt += 1
            now = e
    return cnt

print(solution(n,T))