# 일곱 난쟁이의 키의 합이 100이 됨
# 일곱 난쟁이를 찾는 프로그램?
# 조합을 이용한 전수 조사..?

import sys
input = sys.stdin.readline
from itertools import combinations

A = [int(input()) for _ in range(9)]
tot = sum(A)

for i,j in combinations(A,2):
    if tot - i - j == 100:
        A.remove(i)
        A.remove(j)
        break

A.sort()
print('\n'.join(map(str,A)))