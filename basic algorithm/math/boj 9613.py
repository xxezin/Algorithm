import sys
import math
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())):
    tmp = list(map(int,input().split()))
    n,A = tmp[0],tmp[1:]
    sum = 0
    for i,j in combinations(A,2):
        sum += math.gcd(i,j)
    print(sum)