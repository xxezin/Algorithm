import math
S,E = map(int,input().split())
A = [0]*(E+1)

for i in range(2,E+1):
    A[i] = i

for i in range(2,int(math.sqrt(E))+1):
    if A[i] == 0:
        continue
    for j in range(i+i,E+1,i):
        A[j] = 0

for i in range(S,E+1):
    if A[i] != 0:
        print(A[i])