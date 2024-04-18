num = list(input())
A = [0 for _ in range(10)]
answer = 0
for i in num:
    if int(i) != 6 and int(i) != 9:
        A[int(i)] += 1
        
    else:
        if A[6] <= A[9]:
            A[6] += 1
        else:
            A[9] += 1

print(max(A))