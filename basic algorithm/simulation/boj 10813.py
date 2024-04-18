# N개의 바구니. 각 바구니에는 1~N번까지 번호가 매겨져있음
# 바구니에는 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = dict()
for i in range(1,n+1):
    dic[i] = i
    
for _ in range(m):
    a,b = map(int,input().split())
    dic[a],dic[b] = dic[b],dic[a]
    
print(' '.join(map(str,dic.values())))