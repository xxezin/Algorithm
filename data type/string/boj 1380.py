import sys
from collections import defaultdict
input = sys.stdin.readline

cnt = 1
answer = []
while True:

    tmp = int(input())
    if tmp == 0:
        break
    
    dic = {}
    for i in range(tmp):
        dic[i+1] = input().rstrip()
    
    num_dic = defaultdict(int)
    for i in range(2*tmp-1):
        num,alp = input().split()
        num_dic[num] += 1
    
    for k,v in num_dic.items():
        if v == 1:
            print(cnt,dic[int(k)])
            break
        
    cnt += 1
    
