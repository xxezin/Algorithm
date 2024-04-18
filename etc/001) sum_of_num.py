# N개의 숫자가 공백 없이 써있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오

# 1번째 줄에 숫자의 개수 N(1<= N <= 100),
# 2번째 줄에 숫자 N개가 공백 없이 주어진다.

## pseudo code ##
"""n값 받기
numbers 변수에 list 함수 이용해 숫자를 한자리씩 나눠 받기
sum 변수 선언
for numbers 탐색 :
    sum 변수에 numbers에 있는 각 자릿수를 가져와 더하기
sum 출력"""

# code
n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i)

print(sum)