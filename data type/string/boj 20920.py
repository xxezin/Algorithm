from collections import defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = defaultdict(int)
for _ in range(n):
    tmp = input().rstrip()
    if len(tmp) >= m:
        dic[tmp] += 1

A = sorted(dic.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in A:
    print(i[0])