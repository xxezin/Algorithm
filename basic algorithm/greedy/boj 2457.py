import sys
inpurt = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

def solution(n,A):
    result = 0
    now_a, now_b = 3, 1
    
    