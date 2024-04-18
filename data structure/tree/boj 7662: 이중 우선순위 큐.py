# 삽입 : 데이터 삽입
# 삭제 : 우선순위가 가장 높은 것 삭제 or 가장 낮은 것 삭제
# 정수만 저장됨. 정수 자체가 우선순위

import sys
input = sys.stdin.readline
from collections import heapq

t = int(input())

def func(f, now):
    if f=='I':






for _ in range(t):
    k = int(input())
    tree = []
    while k >0:
        com,node = input().split()
        if com=='D':
            if tree == []:
                continue
            elif node==