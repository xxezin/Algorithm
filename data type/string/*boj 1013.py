import re
import sys
input = sys.stdin.readline

T = int(input())
A = []
for _ in range(T):
    s = input().rstrip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(s)
    if m:
        print("YES")
    else:
        print("NO")