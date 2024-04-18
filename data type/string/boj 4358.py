import sys
input = sys.stdin.readline
from collections import defaultdict

dic = defaultdict(int)
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    
    dic[tree] += 1
    cnt += 1

dic = sorted(dic.items(),key=lambda x:x[0])
for k,v in dic:
    print(k,f'{(v/cnt)*100:.4f}')