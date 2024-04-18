import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = {}

for i in range(n):
    p,lc,rc = input().split()
    tree[p] = [lc,rc]

# # 레벨 순회
# def level():
#     q = deque('A')
    
#     while q:
#         now = q.popleft()
#         print(now,end='')
#         if tree[now][0]:
#             q.append(tree[now][0])
#         if tree[now][1]:
#             q.append(tree[now][1])
    
# 전위 순회
def preOrd(now):
    if now =='.':
        return
    print(now,end='')
    preOrd(tree[now][0])
    preOrd(tree[now][1])
        
# 중위 순회
def inOrd(now):
    if now == '.':
        return
    inOrd(tree[now][0])
    print(now,end='')
    inOrd(tree[now][1])

# 후위 순회
def postOrd(now):
    if now == '.':
        return
    postOrd(tree[now][0])
    postOrd(tree[now][1])
    print(now,end='')

preOrd('A')
print()
inOrd('A')
print()
postOrd('A')