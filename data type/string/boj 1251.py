from itertools import combinations
A = input().rstrip()
n = len(A)

S = set()

for i,j in combinations(range(1,n),2):
    S.add(A[:i][::-1] + A[i:j][::-1] + A[j:][::-1])

S = sorted(S)
print(S[0])