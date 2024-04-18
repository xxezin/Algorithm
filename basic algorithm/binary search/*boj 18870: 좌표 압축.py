import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
D = sorted(set(A))

dic = {}
for i in range(len(D)):
    dic[D[i]] = i

for i in A:
    print(dic[i], end=' ')