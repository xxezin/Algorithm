import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = list(map(int,input().split()))
S = [0]*N
C = [0]*M
S[0] = A[0]
answer = 0

for i in range(1,N-1): # 합배열 생성
    S[i] = S[i-1]+A[i]

for i in range(0,N-1): # M 값으로 나머지 연산을 수행해 값을 업데이트
    remainder = S[i]%M
    if remainder == 0: # 우선 변경된 합 배열에서 원소 값이 0인 갯수 산출
        answer += 1    # 원소 값이 0이라는 뜻은 원본 리스트의 0부터 i까지의 구간 합이
    C[remainder] +=1   # 이미 M으로 나누어 떨어진다는 뜻이다

for i in range(0,M-1):
    if C[i] > 1:
        answer += (C[i] * C[i-1] // 2) # /연산을 하면 answer 변수가 float 형태로 나와 오답처리됨

print(answer)

