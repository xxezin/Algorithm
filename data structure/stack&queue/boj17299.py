from collections import Counter

N = int(input())

A = list(map(int,input().split()))
counter = Counter(A)
B = [-1]*(N)

stack = []

for i in range(N):
    while stack and counter[stack[-1][1]] < counter[A[i]]:
        idx, value = stack.pop()
        B[idx] = A[i]
    stack.append([i,A[i]])
    
print(' '.join(map(str,B)))