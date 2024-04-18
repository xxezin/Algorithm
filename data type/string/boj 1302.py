import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
A = [input().rstrip() for _ in range(n)]
dic = Counter(A)
M = dic.most_common(1)[0][1] # 가장 빈번하게 등장

most = []
for k,v in dic.items():
    if v == M:
        most.append(k)

print(sorted(most)[0])