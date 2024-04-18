import sys
input = sys.stdin.readline

n = int(input())
A = [input().rstrip() for _ in range(n)] # 터널 in
B = [input().rstrip() for _ in range(n)] # 터널 out

answer = 0
for i in range(n):
    set_bef = set(A[:i])
    set_aft = set(B[:B.index(A[i])])
    
    if set_bef != set_bef & set_aft:
        answer += 1
print(answer)