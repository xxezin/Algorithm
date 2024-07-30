import sys
from collections import deque
input = sys.stdin.readline

# def level():
#     q = deque(tree["A"])
#     while q:
#         now = q.popleft()
#         print(now, end='')
        
#         if tree[now][0]:
#             q.append(tree[now][0])
#         if tree[now][1]:
#             q.append(tree[now][1])
            
def preOrd(now):
    if now == '.':
        return
    print(now, end='')
    preOrd(tree[now][0])
    preOrd(tree[now][1])
        
def inOrd(now):
    if now == '.':
        return
    inOrd(tree[now][0])
    print(now, end='')
    inOrd(tree[now][1])

def postOrd(now):
    if now == '.':
        return
    postOrd(tree[now][0])
    postOrd(tree[now][1])
    print(now, end='')

n = int(input())
tree = dict()

for i in range(n):
    p, lc, rc = input().split()
    tree[p] = [lc, rc]

# level()
preOrd("A")
print()
inOrd("A")
print()
postOrd("A")