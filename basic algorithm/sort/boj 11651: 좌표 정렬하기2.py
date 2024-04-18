import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split( ))) for _ in range(n)]
A.sort(key=lambda x:(x[1],x[0]))
for i,j in A:
    print(f'{i} {j}',end='\n')