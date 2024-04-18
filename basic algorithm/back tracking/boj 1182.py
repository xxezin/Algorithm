def back(cnt,tot):
    global answer
    if cnt == n:
        if tot == s:
            answer += 1
            return
        return
        
    back(cnt+1,tot)
    back(cnt+1,tot+arr[cnt])

n,s = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

back(0,0)
if s == 0:
    print(answer-1)
else:
    print(answer)