def fac(v):
    if v==0 or v==1:
        return 1
    else:
        return v * fac(v-1)

n = int(input())
A = str(fac(n))
cnt = 0
for i in range(len(A)-1,-1,-1):
    if A[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break
else:
    print(0)