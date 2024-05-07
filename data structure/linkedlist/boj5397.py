# 강산이의 비밀번호를 알아내는 프로그램을 작성
# input : 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
# 강산이가 입력한 순서대로 길이가 L인 문자열이 주어짐 (1 ≤ L ≤ 1,000,000)

import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    tmp = list(input().rstrip())
    
    A = []
    B = []
    
    for i in tmp:
        if i == '<' and A:
            B.append(A.pop())
        elif i == '>' and B:
            A.append(B.pop())
        elif i == '-' and A:
            A.pop()
        elif i.isalnum():
            A.append(i)
        
    print(''.join(A)+''.join(B[::-1]))