# 그룹 단어 : 단어에 존재하는 모든 문자에 대해, 
#             각 문자가 연속해서 나타나는 경우

# 예) 
# ccazzzzbb : yes
# kin : yes
# aabbbccb : no (b가 떨어져 있음)

# 입력 : 단어 N개
# 출력 : 단어의 갯수

# 필요 기능 1 : 문자가 연속해서 나타나는지 여부
# 필요 기능 2 : 그룹 단어 갯수 출력

# 단어는 알파벳 소문자로만 되어있고, 중복되지 않으며, 길이는 최대 100
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
words = []
for i in range(n):
    words.append(str(input()))

cnt = 0 # 그룹단어가 아닌 갯수
def group(word):
    global cnt

    A = list(word)
    B = deque()
    
    B.append(A[0])
    for _ in A:
        if B[-1] != _:
            if _ not in B:
                B.append(_)
            else:
                cnt +=1
                break

for word in words:
    group(word)

print(n-cnt)