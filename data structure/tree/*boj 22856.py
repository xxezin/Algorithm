import sys
from sys import stdin
sys.setrecursionlimit(10**8)
input = stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
def inOrd(node):
    if node.left != -1:
        inOrd(tree[node.left])
    A.append(node.data)
    if node.right != -1:
        inOrd(tree[node.right])

def similar_inOrd(node):
    global cnt
    
    if node.left != -1:
        similar_inOrd(tree[node.left])
        cnt += 1
    
    if node.data == A[-1]:
        print(cnt)
        exit(0)
        
    cnt += 1
    if node.right != -1:
        similar_inOrd(tree[node.right])
        cnt += 1

n = int(input())
tree = {}
for i in range(n):
    data, left, right = map(int,input().split())
    tree[data] = Node(data,left,right)

A = []
cnt = 0
inOrd(tree[1])
similar_inOrd(tree[1])