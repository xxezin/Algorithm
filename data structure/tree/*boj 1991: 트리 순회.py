# 전위 : 루트, 왼쪽 자식, 오른쪽 자식
# 중위 : 왼쪽 자식, 루트, 오른쪽 자식
# 후위 : 왼쪽 자식, 오른쪽 자식, 루트


import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left,right]

def preOrder(now): # 루트,왼,오
    if now =='.': #
        return
    print(now,end='')
    preOrder(tree[now][0])
    preOrder(tree[now][1])

def inOrder(now): # 왼,루트,오
    if now =='.':
        return
    inOrder(tree[now][0])
    print(now,end='')
    inOrder(tree[now][1])

def postOrder(now): # 왼,오,루트
    if now =='.':
        return
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now,end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')