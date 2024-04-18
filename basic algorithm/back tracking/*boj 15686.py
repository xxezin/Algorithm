import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
graph,home,chicken = [],[],[]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            home.append((i,j))
        elif tmp[j] == 2:
            chicken.append((i,j))

answer = n * 2 * len(home)
for com in list(combinations(chicken,m)):
    dist = 0
    for a,b in home: # 각 집마다의 치킨 거리 구하기
        tmp = n * 2
        for x,y in com:
            tmp = min(tmp, abs(x-a)+abs(y-b))
        dist += tmp
    answer = min(answer,dist) # M개 골랐을때 치킨 거리 작은걸로 갱신
    
print(answer)