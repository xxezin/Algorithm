# counting sort 이용 # sort 함수보다 시간 더 걸림...
import sys
input = sys.stdin.readline

n = int(input())
cnt = [0]*(2000001)

for i in range(n):
    a = int(input())
    cnt[a+1000000] +=1

for i in range(len(cnt)):
    while cnt[i]:
        print(i-1000000,end='\n')
        cnt[i] -=1