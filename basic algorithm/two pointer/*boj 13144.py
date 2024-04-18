n = int(input())
A = list(map(int,input().split()))

s,e,cnt = 0,0,0
vis = [False]*(100001)

while s <= e and e < n:
    if not vis[A[e]]: # 유니크한 요소면
        vis[A[e]] = True
        e += 1
        cnt += e-s
        
    else: # 중복되는 요소면 s포인터 한칸 옮김
        while vis[A[e]]:
            vis[A[s]] = False
            s += 1
            
print(cnt)