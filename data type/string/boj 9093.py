T = int(input())
for _ in range(T):
    A = list(map(str,input().rstrip().split()))
    for i in range(len(A)):
        A[i] = A[i][::-1]
    
    print(' '.join(A))