import sys
input = sys.stdin.readline

dic = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
cnt = 0 # 학점 총합
answer = 0 # 학점*점수
while True:
    try:
        subject, a, b = input().rstrip().split()
        if b != 'P':
            cnt += float(a)
            answer += float(a)*float(dic[b])    
    except:
        break
print(answer/cnt)