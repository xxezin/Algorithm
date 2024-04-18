import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}

for _ in range(n):
    group = input().rstrip()
    num = int(input())

    for i in range(num):
        tmp = input().rstrip()
        if group not in dic:
            dic[group] = [tmp]
            dic[tmp] = group
        else:
            dic[group] += [tmp]
            dic[tmp] = group
    
for _ in range(m):
    name = input().rstrip()
    ques = int(input())
    if ques == 0: # 팀 이름이 주어짐
        print('\n'.join(sorted(dic[name])))
    else: # 멤버 이름이 주어짐
        print(dic[name])