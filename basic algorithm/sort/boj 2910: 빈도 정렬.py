n,c = map(int,input().split())
A = list(map(int,input().split()))

cnt = {}
for i in A:
    if i in cnt:
        cnt[i] +=1
    else:
        cnt[i] =1

cnt = dict(sorted(cnt.items(), key=lambda x:x[1], reverse=True))

for i in cnt:
    while cnt[i]:
        print(i,end=' ')
        cnt[i] -=1
