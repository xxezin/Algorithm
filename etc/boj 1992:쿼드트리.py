import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(str,input().rstrip())) for _ in range(n)]
result = ""

def check(row,col,n):
    global result
    loop = True
    curr = paper[row][col]

    for i in range(row,row+n):
        for j in range(col,col+n):
            if paper[i][j] != curr:
                loop = False
                result+="("
                new_n = n//2
                check(row,col,new_n)
                check(row,col+new_n,new_n)
                check(row+new_n,col,new_n)
                check(row+new_n,col+new_n,new_n)
                result+=")"
                break
        if not loop:
            break
    if loop:
        result += paper[row][col]

    
    return result

print(check(0,0,n))