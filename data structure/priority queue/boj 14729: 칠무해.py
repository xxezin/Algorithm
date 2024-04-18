import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = [] # 학생 성적 우선순위큐
for i in range(n):
    heapq.heappush(A,float(input()))

for i in range(7):
    print("{:.3f}".format(heapq.heappop(A)))