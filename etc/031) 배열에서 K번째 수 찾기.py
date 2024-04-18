N = int(input())
K = int(input())
start = 1
end = K
ans = 0

# 이진 탐색
while start <= end:
    middle = (start+end)//2 # 중앙 값
    count = 0 # 중앙값보다 작은 수
    for i in range(1,N+1): # 갯수 세기
        count += min(int(middle/i),N) # 작은 수 카운트의 핵심 로직!
    if count < K:
        start = middle+1
    else:
        end = middle-1
        ans = middle

print(ans)
