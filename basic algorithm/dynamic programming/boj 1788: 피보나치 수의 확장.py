n = int(input())
abs_n = abs(n)
D = [0]*(1000001)

D[0] = 0
D[1] = 1

if n>=2:
    for i in range(2,n+1):
        D[i] = (D[i-1]+D[i-2])%1000000000
elif n<=-2:
    for i in range(2,abs_n+1):
        if -D[i-1]+D[i-2]<0:
            D[i] = abs(-D[i-1]+D[i-2])%1000000000
            D[i]= -D[i]
        else:
            D[i] = (-D[i-1]+D[i-2])%1000000000

# 확인 후 프린트
if D[abs_n]>0:
    print(1)
    print(D[abs_n])
elif D[abs_n]==0:
    print(0)
    print(D[abs_n])
else:
    print(-1)
    print(abs(D[abs_n]))