import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

A.sort()
for i in range(n):
    print(' '.join(map(str,A[i])))

# 소요 시간 : 6분 30초