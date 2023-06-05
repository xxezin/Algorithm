# N*N개의 수가 N*N 크기의 표에 채워져 있다.
# 표 안의 수 중에서 (X1,Y1)에서 (X2,Y2)까지의 합을 구하려 한다.
# X는 행, Y는 열을 의미한다.
# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때 이를 처리하는 프로그램을 작성하시오

# 1번째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다(1<=N<=1024, 1<=M<=100,000).
# 2번째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다.
# 다음 M개의 줄에는 4개의 정수 X1,Y1,X2,Y2가 주어지며,
# (X1,Y1)에서 (X2,Y2)까지의 합을 구해 출력해야 한다.
# 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수다. (X1<=X2, Y1<=Y2)

## pseudo code ##
"""
n(표의 크기), m(질의 횟수)을 받는다
A(원본 리스트), D(합 배열)

for i -> n번 반복:
    원본 리스트 데이터 저장

for i -> 1...n:
    for j -> 1...n:
        합 배열 저장
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

for i -> m번 반복:
    질의에 대한 결과 계산 및 출력
    결과 = D[X2][Y2] - D[X2][Y1-1] - D[X1-1][Y2] + D[X1-1][Y1-1]
"""

# code
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0]+[int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        # 합 배열 구하기
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    X1,Y1,X2,Y2 = map(int, input().split())
    # 구간 합 배열로 질의 답변
    result = D[X2][Y2] - D[X2][Y1-1] - D[X1-1][Y2] + D[X1-1][Y1-1]
    print(result)