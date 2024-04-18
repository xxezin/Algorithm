import heapq
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
items = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

items.sort()
bag.sort()

ans = 0
pos = [] # 현재 가방보다 무게가 작은 것들
for i in bag:
    while items and items[0][0] <= i:
        heapq.heappush(pos,-items[0][1])
        heapq.heappop(items)

    if pos:
        ans += abs(heapq.heappop(pos))

print(ans)
