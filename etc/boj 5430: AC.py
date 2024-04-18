from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1].split(",")
    queue = deque(arr)

    if n==0:
        queue = []

    reverse_flag = False
    error_flag = False

    for j in p:
        if j== 'R':
              reverse_flag = not reverse_flag

        elif j== 'D':
            if len(queue) > 0:
                if reverse_flag:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                error_flag = True
                break
    
    if error_flag:
        print("error")
    else:
        if reverse_flag:
            queue.reverse()
            print("["+",".join(queue)+"]")
        else:
            print("["+",".join(queue)+"]")


