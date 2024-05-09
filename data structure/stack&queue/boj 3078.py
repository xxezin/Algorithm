import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N,K = map(int,input().split())
q = deque()
dict = defaultdict(int)
answer = 0

for i in range(N):
    tmp = len(input().rstrip()) # 길이로 큐에 저장
    
    if len(q) > K:
        tmp2 = q.popleft()
        dict[tmp2] -= 1
        answer += dict[tmp2]
 
    q.append(tmp)
    dict[tmp] += 1

while q:
    tmp2 = q.popleft()
    dict[tmp2] -= 1
    answer += dict[tmp2]
    
print(answer)