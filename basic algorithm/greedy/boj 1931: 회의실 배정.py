import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
A.sort(key=lambda x:(x[1],x[0])) # 빨리 끝나는 순, 끝나는 시간이 같다면 시작하는 시간이 같은 순

cnt = 1
now = A[0][1]

for i in range(1,n):
    if A[i][0] >= now:
        cnt +=1
        now = A[i][1]

print(cnt)