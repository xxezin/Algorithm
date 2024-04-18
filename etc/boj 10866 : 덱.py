import sys
input = sys.stdin.readline

N = int(input())
MX = 100001
head = MX
tail = MX
deque = [0]*(2*MX+1)

for i in range(N):
    A = input()
    if A.startswith('push_front'):
        head-=1
        deque[head]= int(A[10::])

    elif A.startswith('push_back'):
        deque[tail] = int(A[9::])
        tail+=1

    elif A.startswith('pop_front'):
        if tail-head == 0:
            print(-1)
        else:
            print(deque[head])
            head+=1

    elif A.startswith('pop_back'):
        if tail-head == 0:
            print(-1)
        else:
            print(deque[tail-1])
            tail-=1

    elif A.startswith('size'):
        print(tail-head)

    elif A.startswith('empty'):
        if tail-head == 0:
            print(1)
        else:
            print(0)

    elif A.startswith('front'):
        if tail-head == 0:
            print(-1)
        else:
            print(deque[head])

    elif A.startswith('back'):
        if tail-head == 0:
            print(-1)
        else:
            print(deque[tail-1])