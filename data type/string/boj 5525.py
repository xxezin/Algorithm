import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
S = input().rstrip()
P = "IOI"+"OI"*(n-1)

cnt = 0
for i in range(0,m-len(P)+1):
    if S[i:i+3] != "IOI":
        continue
    if S[i:i+len(P)] == P:
        cnt += 1
print(cnt)
