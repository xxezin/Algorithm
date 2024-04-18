n,m = map(int,input().split())
arr = [0]*(m)
used = [False]*(n+1)

def back(k):
    if k == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        if not used[i]:
            used[i] = True
            arr[k] = i
            back(k+1)
            used[i] = False

back(0)