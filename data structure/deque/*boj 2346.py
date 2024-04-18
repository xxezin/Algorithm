from collections import deque

n = int(input())
balloon = deque(enumerate(map(int,input().split())))

for i in range(n):
    idx,tmp = balloon.popleft()
    print(idx+1,end=' ')
    if tmp > 0:
        balloon.rotate(-(tmp-1)) # 왼쪽 회전
        print(balloon)
    else:
        balloon.rotate(-tmp) # 오른쪽 회전
        print(balloon)