import sys
input = sys.stdin.readline

n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0,0,0

papers = [list(map(int,input().split())) for _ in range(n)]

def check(row,col,n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = papers[row][col]

    for i in range(row,row+n):
        for j in range(col,col+n):
            if papers[i][j] != curr:
                next_n = n//3
                check(row,col,next_n)
                check(row,col+next_n,next_n)
                check(row,col+2*next_n,next_n)
                check(row+next_n,col,next_n)
                check(row+next_n,col+next_n,next_n)
                check(row+next_n,col+2*next_n,next_n)
                check(row+2*next_n,col,next_n)
                check(row+2*next_n,col+next_n,next_n)
                check(row+2*next_n,col+2*next_n,next_n)
                return
            
    if curr == -1:
        minus_cnt +=1
    elif curr == 0:
        zero_cnt +=1
    elif curr == 1:
        plus_cnt +=1

    return

check(0,0,n)