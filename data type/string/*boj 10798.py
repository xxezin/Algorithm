A = []
for _ in range(5):
    A.append(list(input()))

M = max(list(map(len,A))) # 가장 긴 길이 찾기
for i in range(5):
    tmp = len(A[i])
    if tmp < M:
        A[i] += ["" for _ in range(M-tmp)]

A = list(map(list,zip(*A)))
new = sum(A,[])
print(''.join(new))