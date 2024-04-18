n = int(input())
A = list(map(int,input().split()))
D = A[:]

for i in range(n): # n = 10 이라고 치면
    for j in range(i): # 이전의 숫자들 중에
        if A[i] > A[j]: # 자기보다 작으면
            D[i] = max(D[i],D[j]+A[i]) # 이전 최댓값+자기자신 업데이트 하며 비교

print(max(D))