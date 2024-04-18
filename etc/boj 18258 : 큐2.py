import sys
input = sys.stdin.readline

N = int(input())
queue = [0]*2000001
head = 1
tail = 1

for i in range(N):
    A = input()
    if A.startswith('push'):
        queue[tail] = int(A[5::])
        tail+=1
    elif A.startswith('pop'):
        if head==tail:
            print(-1)
        else:
            print(queue[head])
            head+=1
    elif A.startswith('size'):
        print(tail-head)
    elif A.startswith('empty'):
        if head==tail:
            print(1)
        else:
            print(0)
    elif A.startswith('front'):
        if head==tail:
            print(-1)
        else:
            print(queue[head])
    elif A.startswith('back'):
        if head==tail:
            print(-1)
        else:
            print(queue[tail-1])