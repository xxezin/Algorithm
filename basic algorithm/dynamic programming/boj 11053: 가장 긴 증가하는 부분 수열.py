n = int(input())
A = list(map(int,input().split()))
D = [1]*(1001) # 자기 자신을 포함해 만들 수 있는 LIS 길이 저장
# 자기 자신을 포함하므로 테이블을 1로 초기화


for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[i],D[j]+1)

print(max(D))