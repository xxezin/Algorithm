# code
N = int(input())
M = int(input())
A = list(input())
i = 0
j = N-1
count = 0

while i < j :
    if A[i]+A[j] < M :
        i+=1
    elif A[i]+A[j] > M :
        j-=1
    else :
        count +=1
        i+=1
        j-=1

print(count)
