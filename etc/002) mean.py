# 세준이는 기말고사를 망쳤다. 그래서 점수를 조작해 집에 가져가기로 결심했다.
# 일단 세준이는 자기 점수 중 최댓값을 골랐다. 그런 다음 모든 점수를
# 점수/M *100으로 고쳤다.
# 세준이의 성적을 이 방법으로 계산했을 때 새로운 평균을 구하는 프로그램을 작성해라

# 1번째 줄에 시험을 본 과목의 개수 N이 주어지며, 해당 값은 1000보다 작거나 같다.
# 2번째 줄에 세준이의 현재 성적이 주어진다. 해당 값은 100보다 작거나 같은,
# 음이 아닌 정수고, 적어도 1개의 값은 0보다 크다.

## pseudo code ##
"""n에 과목 수 입력
scores에 List로 점수 받기
max_score에 최댓값 저장
sum에 총합 저장
sum/max_score *100 /n"""

# code
n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
sum = sum(scores)
print(sum/max_score*100/n)
