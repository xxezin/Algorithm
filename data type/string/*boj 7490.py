def func(cnt,ans):
    if cnt == n+1:
        calc(ans)
        return
    
    for k in {" ","+","-"}:
        func(cnt+1,ans+k+str(cnt))
        
def calc(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        print(ans)
        
T = int(input())
for _ in range(T):
    n = int(input())
    answer = []
    func(2,'1')
    print()