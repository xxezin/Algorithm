## pseudo code ##
"""
n 입력받기 (수열의 갯수)
m 입력받기 (나누어 떨어져야 하는 수)
A 입력받기 (원본 수열 저장 리스트)
S 선언하기 (합 배열)
C 선언하기 (같은 나머지의 인덱스를 카운트하는 리스트)
anwer 선언하기 (정답 변수)

for i -> 1...n-1 :
    S[i] = S[i-1]+A[i] # 합 배열 저장

for i -> 0...n-1 :
    remainder = S[i] %M # 합 배열을 M으로 나눈 나머지 값
    if(remainder==0) 정답을 1 증가
    C[remainder]의 값을 1 증가

for i -> 0...m-1 :
    C[i](i가 나머지인 인덱스의 갯수)에서 2가지를 뽑는 경우의 수를 정답에 더하기
    # C[i]개 중 2개를 뽑는 경우의 수 계산 공식은 C[i]*(C[i]-1)/2
"""

# code
import sys
input = sys.stdin.readline
n,m = map(int, input.split())
A = list(map(int, input.split()))
S = [0]*n
C = [0]*m
S[0] = A[0]
answer = 0

for i in range(1,n):
    S[i] = S[i-1] + A[i] # 합 배열 저장

for i in range(n):
    remainder = S[i] %m  # 합 배열을 M으로 나눈 나머지 값
    if remainder == 0 : # 0~i까지의 구간 합 자체가 0일 때 정답에 더하기
        answer +=1
    C[remainder] += 1   # 나머지가 같은 인덱스의 갯수 값 증가시키기

for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수 더하기
    if C[i] > 1:
        answer += (C[i]*(C[i]-1)//2)

print(answer)