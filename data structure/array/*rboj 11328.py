import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    A,B = map(str,input().split())
    A = sorted(A)
    B = sorted(B)
    
    print("Possible" if A==B else "Impossible")