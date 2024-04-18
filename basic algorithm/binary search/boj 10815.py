import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
A.sort()

m = int(input())
B = list(map(int,input().split()))

C = [0]*m

for i in range(m):
    start, end = 0, n-1
    flag = False
    while start <= end:
        midi = (start+end)//2
        midv = A[midi]
             
        if B[i] > midv:
            start = midi + 1
        elif B[i] < midv:
            end = midi - 1
        else:
            C[i] = 1
            break
            
print(' '.join(map(str,C)))