from collections import deque
N,L = map(int,input().split())
mydeque = deque()
now = list(map(int,input().split()))

# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i)) # 현재 원소 추가
    if mydeque[0][1] <= i-L: # 범위에서 벗어난 인덱스를 가진 값은 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0],end=' ')

# 데크는 처음이라 이해하기 좀 어려웠다..