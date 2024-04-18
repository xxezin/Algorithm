import sys
input = sys.stdin.readline

n_a, n_b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

ans = sorted(list(A-B))

print(len(ans))
print(' '.join(map(str,ans)))