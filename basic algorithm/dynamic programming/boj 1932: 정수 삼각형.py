n = int(input())
D = [[0]*501 for _ in range(501)]
A = [0]
for i in range(n):
    A.append(list(map(int,input().split())))


D[1][0] = A[1][0]
ans = D[1][0]

if n>=2:
    D[2][0] = D[1][0] + A[2][0]
    D[2][1] = D[1][0] + A[2][1]
    ans = max(D[2][0],D[2][1])
    for i in range(3,n+1):
        for j in range(0,i):
            if j==0:
                D[i][j] = D[i-1][0]+A[i][0]
                ans = max(ans,D[i][j])
            elif 0<j<i-1:
                D[i][j] = max(D[i-1][j-1],D[i-1][j])+A[i][j]
                ans = max(ans,D[i][j])
            elif j==i-1:
                D[i][j] = D[i-1][j-1]+A[i][j]
                ans = max(ans,D[i][j])

print(ans)