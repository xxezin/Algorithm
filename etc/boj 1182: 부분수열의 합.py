N,S = map(int,input().split()) # N: 개수, S: 타겟 합
A = list(map(int,input().split())) # 원소 N개
cnt = 0

def func(cur,ans):
    global cnt
    if cur==N:
        if ans==S:
            cnt+=1
            return
        return
    
    func(cur+1,ans) # 선택하지 않은 경우
    func(cur+1,ans+A[cur]) # 선택한 경우


func(0,0)
if S==0:
    cnt-=1
print(cnt)