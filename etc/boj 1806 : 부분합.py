N,S = map(int,input().split())
A = list(map(int,input().split()))
mylist = []
i=0
j=1

while i<=j and j<=N:
    total = sum(A[i:j])
    if total == S:
        mylist.append(j-i)
        j+=1
    elif total > S:
        i+=1
    elif total < S:
        j+=1

print(min(mylist))
