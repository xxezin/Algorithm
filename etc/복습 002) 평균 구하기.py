# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
M = max(A)
sum = sum(A)

print(sum*100/M/N)