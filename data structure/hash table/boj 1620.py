import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}
for i in range(1,n+1):
    name = input().rstrip()
    dic[name] = i
    dic[i] = name

for i in range(m):
    ques = input().rstrip()
    if ques.isdigit():
        print(dic[int(ques)])
    else:
        print(dic[ques])