m,n = map(int,input().split())
answer = []

import math
def sosu(v):
    if v == 1:
        return False
    for i in range(2,int(math.sqrt(v))+1):
        if v % i == 0:
            return False
    return True

for i in range(m,n+1):
    if sosu(i):
        answer.append(i)
        
print('\n'.join(map(str,answer)))