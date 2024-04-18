# 왼쪽 한칸 이동/ 오른쪽 한칸 이동 연산의 최솟값 출력
# 뽑는건 첫번째 칸만 뽑을 수 있음
from collections import deque

n,m = map(int,input().split())
A = deque([i for i in range(1,n+1)])
P = list(map(int,input().split()))

cnt = 0
for i in P:
    while True:
        if A[0] == i:
            A.popleft()
            break
        
        else:
            if A.index(i) < len(A)/2:
                while A[0] != i:
                    A.append(A.popleft())
                    cnt += 1
            else:
                while A[0] != i:
                    A.appendleft(A.pop())
                    cnt += 1

print(cnt)