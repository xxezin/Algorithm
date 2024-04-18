N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(1,N):
    for j in range(N-i):
        if A[j] > A[j+1] :
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])