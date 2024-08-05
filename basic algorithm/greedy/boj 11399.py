n = int(input())
A = list(map(int,input().split()))

def solution(n,A):
    result = 0
    pre = 0
    
    A.sort()
    for a in A:
        result += (pre+a)
        pre += a
    return result

print(solution(n,A))