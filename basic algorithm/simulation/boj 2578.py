import sys
input = sys.stdin.readline

B = [] # 빙고판
for _ in range(5):
    B += list(map(int,input().split()))

S = [] # 사회자가 부르는 순서
for _ in range(5):
    S += list(map(int,input().split()))

def func(map):
    answer = 0
    for i in range(0,25,5): # 가로 일자 빙고 있는지
        if sum(map[i:i+5]) == 0:
            answer += 1
    for i in range(5): # 세로 일자 빙고 있는지
        if sum(map[i::5]) == 0:
            answer += 1
    if sum(map[0::6]) == 0: # 왼쪽부터 대각선
        answer += 1
    if sum(map[4:21:4]) == 0:
        answer += 1
    
    return answer
            
for i in range(25):
    B[B.index(S[i])] = 0
    if func(B) >= 3:
        print(i+1)
        break