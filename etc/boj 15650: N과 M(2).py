n,m = map(int,input().split())
ans = []
used = [False]*(n+1)


def back(start):
    if len(ans)==m: # 만약 해당하는 답이면 출력
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start,n+1): # 아니면 탐색
        if i not in ans:
            ans.append(i)
            back(i+1)
            ans.pop()


back(1)