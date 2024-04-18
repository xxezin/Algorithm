# 노트북이 있고
# 스티커들이 있음
# 필요 기능 1. 스티커들을 붙이고 싶은데, (가장 왼쪽 위쪽부터 붙임)
# 필요 기능 2. 안붙여지면, 회전해서 붙일 수도 있음 (회전해서 안붙여지면 버림)
# 노트북에서 스티커가 붙은 칸의 수를 출력하는 코드를 짜보려무나

# 입력 : 노트북 세로 n 가로 m (1<=n,m<=40) 스티커 개수 k (1<=k<=100)
#       k개의 스티커들에 대한 정보 0: 스티커 안붙음 1: 스티커 붙음

# 출력 : 주어진 스티커들을 차례대로 붙였을때 노트북에서 스티커가 붙은 칸의 수

import sys
input = sys.stdin.readline


# 놓을 수 있는지 보고 붙이는 기능
def stick(x,y):
    global note
    # 놓을 수 있는지 확인 후 붙이기
    for i in range(r):
        for j in range(c):
            if note[x+i][y+j] == sticker[i][j]==1:
                return False # 붙일 수 없다면 False

    # 붙이기
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==1:
                note[x+i][y+j] = 1
    return True # 붙일 수 있다면 붙이고 return True

# 회전하는 기능 # zip함수 이용
def rotate(sticker):
    sticker = zip(*sticker[::-1])
    return [list(e) for e in sticker]


n,m,k = map(int,input().split())
note = [[0]*m for _ in range(n)] # 노트북 준비
ans = 0

# k개의 스티커 입력
for _ in range(k):
    r,c = map(int,input().split()) # 스티커 열,행
    sticker = [list(map(int,input().split())) for _ in range(r)] # 스티커 모양
    
    for rot in range(4):
        is_paste = False
        for x in range(n-r+1):
            for y in range(m-c+1):
                if stick(x,y): # 붙일 수 있다면
                    is_paste = True
                    break
        
            if is_paste:
                break
        if is_paste:
            break
        else :
            sticker = rotate(sticker)

        
cnt = 0
for i in range(n):
    for j in range(m):
        cnt += note[i][j]

print(cnt)