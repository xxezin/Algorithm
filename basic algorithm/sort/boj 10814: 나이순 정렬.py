import sys
input = sys.stdin.readline

n = int(input())
A = [[0,0] for _ in range(n)]
for i in range(n):
    A[i][0] = input().split()
    A[i][1] = i

A.sort(key=lambda x:(int(x[0][0]), int(x[1]))) # sort 함수 정리 필요

for i in range(n):
    print(' '.join(map(str,A[i][0])))

# 소요 시간 : 15분