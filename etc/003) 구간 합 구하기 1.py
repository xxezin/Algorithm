# 수 N개가 주어졌을 때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램을 작성하시오

# 1번째 줄에 수의 갯수 N(1<=N<=100,000), 합을 구해야 하는 횟수 M(1<=M<=100,000)
# 2번째 줄에 N개의 수가 주어진다.
# 각 수는 1,000보다 작거나 같은 자연수다
# 3번째 줄부터는 M개의 줄에 합을 구해야 하는 구간 i와 j가 주어진다.

## pesudo code ##
"""suNo(숫자 갯수), quizNo(질의 갯수)
numbers 변수에 숫자 데이터 저장
prefix_sum 합 배열 변수 선언
temp 변수 선언

for 저장한 숫자 데이터 차례대로 탐색
    temp에 현재 숫자 데이터 더해 주기
    합 배열에 temp값 저장

for 질의 갯수만큼 반복
    질의 범위 받기(start~end)
    구간 합 출력하기(prefix_sum[end]-prefix_sum[start-1])"""

# code
import sys
input = sys.stdin.readline # 반복문으로 여러줄을 입력 받아야 할 때 시간초과 방지
suNo,quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for j in range(quizNo):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])

