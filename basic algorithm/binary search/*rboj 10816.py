import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
tmp = sorted(list(map(int,input().split())))
dic = defaultdict(int)
for i in tmp:
    dic[i] += 1

m = int(input())
B = list(map(int,input().split()))

# 이분 탐색 아님 - 872ms
# for i in B:
#     if i in dic:
#         print(dic[i],end=' ')
#     else:
#         print(0,end=' ')

# 이분 탐색 - 4360ms
for i in B:
    s,e = 0,len(tmp)-1
    
    while s <= e:
        mid = (s+e)//2
        if i == tmp[mid]:
            print(dic.get(i),end=' ')
            break
        else:
            if i < tmp[mid]:
                e = mid-1
            else:
                s = mid+1
    else:
        print(0,end=' ')