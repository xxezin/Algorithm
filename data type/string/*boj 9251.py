def LCS(X,Y):
    X,Y = " "+X , " "+Y
    for i in range(1,len(X)):
        for j in range(1,len(Y)):
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    return dp[len(X)-1][len(Y)-1]

X = input().rstrip()
Y = input().rstrip()
dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]

print(LCS(X,Y))
