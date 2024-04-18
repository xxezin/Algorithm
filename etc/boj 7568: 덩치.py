# 여러명이 있음
# 키와 몸무게 둘다 크면 덩치 큰것
# 하나는 크고 하나는 작으면 같은 등수(중복 가능)
# 처음 받았던 순서대로 등수 리턴해줌

# 입력 : 사람수, 차례대로 몸무게와 키
# 출력 : 등수 ' '.join

# 등수가 낮다는건 완벽히 덩치가 작다는걸 의미하고
# 등수가 높다는건 완벽히 덩치가 크다는걸 의미함
# 그렇다면 같을 때는?

# sort를 쓰면 인덱스가 섞이는 문제 발생...
# queue...를 써야할까?
# 젤 큰수를 업데이트하면?


import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    cnt = 1
    tmp = A[i]

    for j in range(n):
        if i==j: continue
        elif tmp[0] < A[j][0] and tmp[1] < A[j][1]:
            cnt +=1

    print(cnt,end=' ')