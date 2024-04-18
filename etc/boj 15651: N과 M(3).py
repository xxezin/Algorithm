n,m = map(int,input().split())
ans = []

def func(k):
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        ans.append(i)
        func(i+1)
        ans.pop()

func(1)