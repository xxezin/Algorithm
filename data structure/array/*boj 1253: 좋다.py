n = int(input())
A = list(map(int,input().split()))
A.sort()

result = 0
for k in range(n):
    find = A[k]
    i, j = 0, n-1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(result)
