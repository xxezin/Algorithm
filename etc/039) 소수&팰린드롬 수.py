import math
N = int(input())
A = [0]*(10000001)

for i in range(2,len(A)):
    A[i] = i

for i in range(2,int(math.sqrt(len(A))+1)):
    if A[i] == 0:
        continue
    for j in range(i+i,len(A),i):
        A[j] = 0

# 팰린드롬
def pal(n):
    n_list = list(str(n))
    s = 0
    e = len(n_list) -1
    while (s<e) :
        if n_list[s] != n_list[e]:
            return False
        s +=1
        e -=1
    return True

i = N
while True:
    if A[i] != 0:
        result = A[i]
        if (pal(result)):
            print(result)
            break

    i += 1