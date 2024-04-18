import sys
input = sys.stdin.readline
N,M = map(int,input().split())
numbers = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for num in numbers:
    temp += num
    prefix_sum.append(temp)

for i in range(M):
    s,e = map(int,input().split())
    print(prefix_sum[e]-prefix_sum[s-1])

