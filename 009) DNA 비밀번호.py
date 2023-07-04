# 전역 변수 선언
checkList = [0]*4
myList = [0]*4
checkSecret = 0

# 함수 선언
def myadd(alp):
    global checkList, myList, checkSecret
    if alp == 'A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret +=1
    elif alp =='C':
        myList[1] +=1
        if myList[1] == checkList[1]:
            checkSecret +=1
    elif alp == 'G':
        myList[2] +=1
        if myList[2] == checkList[2]:
            checkSecret +=1
    elif alp == 'T':
        myList[3] +=1
        if myList[3] == checkList[3]:
            checkSecret +=1

def myremove(alp):
    global checkList, myList, checkSecret
    if alp == 'A':
        if myList[0] == checkList[0]:
            checkSecret -=1
        myList[0] -= 1
    elif alp =='C':
        if myList[1] == checkList[1]:
            checkSecret -=1
        myList[1] -= 1
    elif alp == 'G':
        if myList[2] == checkList[2]:
            checkSecret -=1
        myList[2] -= 1
    elif alp == 'T':
        if myList[3] == checkList[3]:
            checkSecret -=1
        myList[3] -= 1

# main code
S,P = map(int,input().split())
result = 0
A = list(input())
checkList = list(map(int,input().split()))

## 첫번째 문자열에 대한 검사
for i in range(4):
    if checkList[i] ==0:
        checkSecret +=1

for i in range(P):
    myadd(A[i])
    if checkSecret ==4:
        result +=1
## 슬라이딩하며 검사
for i in range(P,S):
    j = i-P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        result +=1

print(result)