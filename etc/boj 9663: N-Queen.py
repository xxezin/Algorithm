n = int(input())

used1 = [False]*n
used2 = [False]*(2*n)
used3 = [False]*(2*n)

cnt = 0
def func(cur):
    global cnt
    if cur==n:
        cnt +=1
        return
    for i in range(n):
        if used1[i] or used2[i+cur] or used3[cur-i+n-1]: # 같은열 혹은 대각선에 위치하는지 확인
            continue # 만약 하나라도 True면 아래 실행하지 않고 건너뜀
        
        # 만약 (cur,i)에 퀸을 둘 수 있으면 True로 변경 후 func(cur+1) 호출
        used1[i] = True
        used2[i+cur] = True
        used3[cur-i+n-1] = True
        func(cur+1)

        # 다시 
        used1[i] = False
        used2[i+cur] = False
        used3[cur-i+n-1] = False

func(0)
print(cnt)