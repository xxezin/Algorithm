import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(int(input()) for _ in range(n)))

hap = set()
for i in A:
    for j in A:
        hap.add(i+j)

answer = 0
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if A[i]-A[j] in hap:
            answer = max(A[i],answer)

print(answer)