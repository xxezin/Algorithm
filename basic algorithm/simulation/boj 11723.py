import sys
input = sys.stdin.readline

S = set()
n = int(input())
for _ in range(n):
    tmp = list(input().split())
    if len(tmp) > 1:
        k = int(tmp[1])
        
    if tmp[0]=='add':
        S.add(k)
    elif tmp[0]=='remove':
        S.discard(k)
    elif tmp[0]=='check':
        if k in S:
            print(1)
        else:
            print(0)
    elif tmp[0]=='toggle':
        if k in S:
            S.discard(k)
        else:
            S.add(k)
    elif tmp[0]=='all':
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif tmp[0]=='empty':
        S = set()