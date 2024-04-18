# 절댓값 힙힙힙
# 우선순위 큐를 이용하면 될될될 듯

from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
q = PriorityQueue()

for i in range(N):
    request = int(input())
    if request ==0:
        if q.empty():
            print('0\n')
        else:
            temp = q.get()
            print(str(temp[1])+'\n')
    else:
        q.put((abs(request),request))
