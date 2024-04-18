l,c = map(int,input().split())
A = list(map(str,input().split()))
A.sort()
m = ['a','e','i','o','u']# 모음
m_cnt = 0
z = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'] #자음
z_cnt = 0
ans = []

def func(start):
    global m_cnt,z_cnt
    if len(ans) == l and m_cnt >=1 and z_cnt>=2:
        print(''.join(ans))
        return
    
    for i in range(start,c):
        ans.append(A[i])
        if ans[-1] in m:
            m_cnt+=1
        elif ans[-1] in z:
            z_cnt+=1
        func(i+1)
        if ans[-1] in m:
            m_cnt-=1
        elif ans[-1] in z:
            z_cnt-=1
        ans.pop()

func(0)