n,r,c = map(int,input().split())

def func(n,r,c):
    if n==0:
        return 0
    else:
        half = 2**(n-1)
        if r<half and c<half:
            return func(n-1,r,c)
        elif r<half and c>=half:
            return half*half + func(n-1,r,c-half)
        elif r>=half and c<half:
            return 2*half*half + func(n-1,r-half,c)
        elif r>=half and c>=half:
            return 3*half*half + func(n-1,r-half,c-half)
        
print(func(n,r,c))