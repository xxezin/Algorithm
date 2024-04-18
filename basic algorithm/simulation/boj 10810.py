# N개의 바구니
# M개의 줄에 걸쳐 공을 넣을 방법이 주어짐
# i~j번 바구니까지 k번 번호가 적혀져 있는 공을 넣음

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = dict()
for _ in range(m):
    i,j,k = map(int,input().split())
    for z in range(i,j+1):
        dic[z] = k
        
for i in range(1,n+1):
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')