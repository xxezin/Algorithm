import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = set(input().rstrip() for _ in range(n))

cnt = 0
for _ in range(m):
    s = input().rstrip()
    if s in A:
        cnt += 1
print(cnt)