import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nolis = set(input().rstrip() for _ in range(n))
nolook = set(input().rstrip() for _ in range(m))

answer = sorted(nolis & nolook)
print(len(answer))
print('\n'.join(answer))