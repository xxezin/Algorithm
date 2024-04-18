# -*- coding: utf-8 -*-
# # pseudo code #
# N(수), M(합쳐서 나올 수)
# A(숫자 리스트)
# sum(합)
# count(경우의 수)
#
# 만약 ==M이면 count +=1
# >M이면 i+=1
# <M이면 j+=1
# count 출력

# code #
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = list(map(int,input().split()))
count = 0
i = 0
j = 0

while i<=j and j<=N:
    total = sum(A[i:j])
    if total==M:
        count+=1
        j+=1
    elif total>M:
        i+=1
    elif total<M:
        j+=1

print(count)