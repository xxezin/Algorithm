# 버퍼의 크기 N
# 한 줄에 하나씩 라우터가 처리해야 할 정보가 주어짐

import sys
input = sys.stdin.readline
from collections import deque

buff_size = int(input())
buff = deque()

while True:
    tmp = int(input())
    if tmp == -1:
        break
    
    elif tmp == 0:
        buff.popleft()
    
    else:
        if len(buff) >= buff_size:
            continue
        else:
            buff.append(tmp)

if buff:
    print(' '.join(map(str,buff)))
else:
    print('empty')
