import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}
for i in range(m):
    dic[input().rstrip()] = i

result = sorted(dic.items(), key = lambda x:x[1])

if n > len(result):
    n = len(result)

for i in range(n):
    print(result[i][0])