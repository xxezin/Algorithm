## 점화식을 못찾음...
n = int(input())
A = list(map(int,input().split()))

for i in range(1,n):
    A[i] = max(A[i], A[i] + A[i-1]) # 이전까지 모든 숫자의 합 중 최댓값으로 업데이트!

print(max(A))