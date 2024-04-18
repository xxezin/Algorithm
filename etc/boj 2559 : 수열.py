N,K = map(int,input().split())
A = list(map(int,input().split()))
total = 0

for i in range(K):
    total += A[i]

for i in range(K,N):
    j = i-K
    temp = total
    temp -= A[i]
    temp += A[j]
    if temp > total:
        total = temp


print(total)

