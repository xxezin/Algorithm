## pseudo code
# numlist : 101개의 배열 (0~100)
# N : 숫자 갯수
# mylist : 입력받은 숫자 배열
# 만약 100-지금숫자가 배열에 있으면 값=1
# 끝까지 다 돌고 있었으면 1 없었으면 0

numlist = [0]*101
N = int(input())
mylist = list(map(int,input().split()))
answer = False

for i in mylist:
    if numlist[100-i]==1:
        answer = True
    numlist[i] = 1

if not answer:
    print(0)