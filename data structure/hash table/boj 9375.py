import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for i in range(n):
        cloths, types = input().split()
        if types not in dic:
            dic[types] = 1
        else:
            dic[types] += 1
    
    cnt = 1
    for k in dic.values():
        cnt *= k+1
    print(cnt-1)