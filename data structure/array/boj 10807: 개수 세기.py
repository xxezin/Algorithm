import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
v = int(input())

ans = [0 for _ in range(201)]
for i in A:
    ans[i+100] += 1

print(ans[v+100])