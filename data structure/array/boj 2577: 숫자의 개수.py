import sys
input = sys.stdin.readline

A = [int(input()) for _ in range(3)]
ans = [0 for _ in range(10)]
B = 1

for i in A:
    B *= i

B = list(map(int,str(B)))

for i in B:
    ans[i] +=1

print('\n'.join(map(str,ans)))
