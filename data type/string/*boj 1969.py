# 길이가 같은 두 DNA가 있을 때,
# 각 위치의 뉴클오티드 문자가 다른 것의 개수
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(input().rstrip() for _ in range(n))
A.sort()

dna = ''
for j in range(m):
    value = {'A':0, 'C':0, 'G':0, 'T':0}
    for i in range(n):
        tmp = A[i][j]
        value[tmp] += 1
    dna += max(value ,key=value.get)

answer = 0
for i in range(n):
    for j in range(m):
        if dna[j] != A[i][j]:
            answer += 1

print(dna)
print(answer)