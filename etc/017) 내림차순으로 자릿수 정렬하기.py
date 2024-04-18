import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)): # 남은 정렬에서 가장 앞수
    Max = i
    for j in range(i+1,len(A)): # 남은 정렬에서 가장 큰수
        if A[j] > A[Max]:
            Max = j

    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])