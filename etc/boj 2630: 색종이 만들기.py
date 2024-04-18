import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]

white_cnt,blue_cnt = 0,0

def check(row,col,n):
    global white_cnt, blue_cnt
    curr = paper[row][col]

    for i in range(row,row+n):
        for j in range(col,col+n):
            if paper[i][j] != curr:
                next_n = n//2
                check(row,col,next_n)
                check(row,col+next_n,next_n)
                check(row+next_n,col,next_n)
                check(row+next_n,col+next_n,next_n)

                return
    
    if curr == 0:
        white_cnt +=1
    elif curr == 1:
        blue_cnt +=1

    return

check(0,0,n)
print(white_cnt)
print(blue_cnt)            

