import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = sorted(list(int(input()) for _ in range(n)),reverse=True)

answer = 0
for coin in coins:
    if k == 0:
        break
    if k >= coin:
        answer += k // coin
        k %= coin
print(answer)