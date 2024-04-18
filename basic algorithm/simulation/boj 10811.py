import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = [i for i in range(n+1)]
    
for _ in range(m):
    a,b = map(int,input().split())
    s[a:b+1] = s[a:b+1][::-1]

print(' '.join(map(str,s[1:])))