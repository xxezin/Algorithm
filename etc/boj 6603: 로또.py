import sys
input = sys.stdin.readline
A = []

def func(start):
    if len(ans)== 6:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start,tmp+1):
        ans.append(A[i])
        func(i+1)
        ans.pop()


while A != [0]:
    ans = []
    A = list(map(int,input().split()))
    tmp = A[0]
    func(1)
    print()