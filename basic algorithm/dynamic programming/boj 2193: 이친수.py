n = int(input())
D = [0]*(91)

D[1] = 1
D[2] = 1
for k in range(3,n+1):
    D[k] = D[k-1]+D[k-2]

print(D[n])