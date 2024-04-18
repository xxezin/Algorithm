A,B,C = map(int,input().split())

def recursion(i,j,k):
    if j==1:
        return i%k
    else:
        tmp = recursion(i,j//2,k)
        if j%2==0:
            return (tmp*tmp)%k
        else:
            return (tmp*tmp*i)%k
        
print(recursion(A,B,C))