n = int(input())
A = list(map(int,input().split()))
A.sort()
B = list(map(int,input().split()))
B.sort(reverse=True)

def solution(n,A,B):
    result = 0
    for i,j in zip(A,B):
        result += i*j
        
    return result

print(solution(n,A,B))