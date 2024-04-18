n = int(input())

D = [[0]*10 for _ in range(n+1)]
D[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    for j in range(10):
        D[i][j] = (sum(D[i-1][:j+1]))%10007

print(sum(D[n])%10007)

