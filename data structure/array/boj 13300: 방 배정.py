import sys
input = sys.stdin.readline

n,k = map(int,input().split())
ans = [[0,0] for _ in range(7)]

for _ in range(n):
    sex,grade = map(int,input().split())
    ans[grade][sex] += 1

result = 0
for i,j in ans:
    result += (i//2) + (i%2) + (j//2) + (j%2)

print(result)