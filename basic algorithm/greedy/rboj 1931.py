# 한 개의 회의실!
import sys
input = sys.stdin.readline

n = int(input())
A = list(tuple(map(int,input().split())) for _ in range(n))
A.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간 빠른 순, 시작하는 시간 빠른 순

time, cnt = 0,0
for i in range(n):
    if A[i][0] >= time:
        time = A[i][1]
        cnt += 1
        
print(cnt)