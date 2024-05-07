# 요세푸스 문제
n,k = map(int,input().split())
answer = []

A = [i for i in range(1,n+1)]
idx = 0

while A:
    idx += k-1
    idx %= len(A)
    answer.append(A.pop(idx))

print('<' + ', '.join(map(str,answer)) + '>')