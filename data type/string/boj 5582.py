# python3으로는 시간초과
A = input()
B = input()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
answer = 0

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j],answer)
            
print(answer)