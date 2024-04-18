import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}
for i in range(n):
    url, pas = input().split()
    dic[url] = pas

for i in range(m):
    find = input().rstrip()
    print(dic[find])