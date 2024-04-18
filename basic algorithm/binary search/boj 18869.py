import sys
from bisect import bisect_left
from itertools import combinations
input = sys.stdin.readline

m,n = map(int,input().split())
uni = [list(map(int,input().split())) for _ in range(m)]

uni_set = [[] for _ in range(m)]
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(bisect_left(uni[i],uni[i][j]))
    uni_set[i] = tmp
    
cnt = 0
for i,j in combinations(range(0,m),2):
    if uni_set[i] == uni_set[j]:
        cnt += 1
        
print(cnt)