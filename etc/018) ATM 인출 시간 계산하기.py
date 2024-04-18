N = int(input())
A = list(map(int,input().split()))
S = [0]*N

for i in range(1,N):
    insert_index = i
    insert_value = A[i]
    for j in range(i-1,-1,-1):
        if A[j] < A[i]:
            insert_index = j+1
            break
        if j==0:
            insert_index = 0

    for j in range(i,insert_index,-1):
        A[j] = A[j-1]

    A[insert_index] = insert_value

S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1]+A[i]

sum = 0
for i in range(0,N):
    sum += S[i]

print(sum)