import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
# 소수 구하기 함수
def sosu(N):
    for i in range(2,int(N/2+1)):
        if N % i == 0:
            return False
    return True

# DFS 구현
def DFS(num):
    if len(str(num))==N:
        print(num)
    else:
        for i in range(1,10):
            if i % 2 ==1 and sosu(num*10+i):
                DFS(num*10+i)

# 일의 자리 소수는 2,3,5,7 이므로 4가지 수에서만 시작
DFS(2)
DFS(3)
DFS(5)
DFS(7)