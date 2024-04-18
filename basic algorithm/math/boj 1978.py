import math
n = int(input())
A = map(int,input().split())

def sosu(v):
    if v == 1:
        return 0
    
    for i in range(2,int(math.sqrt(v))+1):
        if v % i == 0:
            return 0
    
    return 1

answer = 0
for a in A:
    answer += sosu(a)
print(answer)