import sys
input = sys.stdin.readline

def func(n,A):

    D = [[0,0,0] for _ in range(n)]
    D[1][0] = A[1][0] + A[0][1]
    D[1][1] = min(D[1][0],A[0][1],A[0][1]+A[0][2]) + A[1][1]
    D[1][2] = min(D[1][1],A[0][1],A[0][1]+A[0][2]) + A[1][2]

    for i in range(2,n):
        D[i][0] = min(D[i-1][0],D[i-1][1])+A[i][0]
        D[i][1] = min(min(D[i-1]),D[i][0])+A[i][1]
        D[i][2] = min(D[i-1][1],D[i-1][2],D[i][1])+A[i][2]

    print(str(k)+". "+str(D[-1][1]))

if __name__ == "__main__":
    k = 0
    while True:
        n = int(input())
        if n==0:
            break
        graph = [list(map(int,input().split())) for _ in range(n)]
        k+=1
        func(n,graph)