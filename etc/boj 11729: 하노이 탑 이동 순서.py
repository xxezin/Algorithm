import sys

K = int(input())

def func(a,b,n):
    if n==1:
        sys.stdout.write('{0} {1}\n'.format(a,b))

    else:
        func(a,6-a-b,n-1)
        sys.stdout.write('{0} {1}\n'.format(a,b))
        func(6-a-b,b,n-1)
    
print(2**K-1)
func(1,3,K)

