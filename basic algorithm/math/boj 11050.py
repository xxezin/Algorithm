n,k = map(int,input().split())

def fac(v):
    if v == 0 or v == 1:
        return 1
    else:
        return v * fac(v-1)
    
print(fac(n)//(fac(n-k)*fac(k)))