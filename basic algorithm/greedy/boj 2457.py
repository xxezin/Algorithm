import sys
from collections import deque
inpurt = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append([a*100+b, c*100+d])
A = deque(sorted(A, key=lambda x:(x[0],x[1])))

cnt = 0
end = 301 # 현재 날짜

while A:
    if end >= 1201 or A[0][0] > end:
        break
    
    nxt_end = -1
    while A:
        if A[0][0] <= end: # 현재 날짜보다 시작 날짜가 작고
            if nxt_end <= A[0][1]: # 종료 날짜가 다음 종료일보다 크면(가장 나중의 종료일 찾기)
                nxt_end = A[0][1]
                
            A.popleft()
        else:
            break
    
    end = nxt_end
    cnt += 1
    
if end < 1201:
    print(0)
else:
    print(cnt)