import sys
from collections import deque
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수
for _ in range(T):
    p = list(input().strip()) # 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    X = input().strip()[1:-1].split(",")
    q = deque(X)

    Rflag = False # 뒤집힌 상태인지 여부
    Eflag = False # 에러 발생 여부
    
    if n == 0:
        q = deque()
    
    for func in p:      
        if func == 'R': # 뒤집기
            Rflag = not Rflag
            
        else: # 버리기
            if len(q) > 0:
                if Rflag: # 뒤집은 상태면 끝 숫자 두개 삭제
                    q.pop()

                else:
                    q.popleft()

            else:
                Eflag = True
                break
                
    
    if Eflag:
        print("error")
    else:
        if Rflag:
            q.reverse()
            print("["+",".join(q)+"]")
        else:
            print("["+",".join(q)+"]")