n = int(input())
A = list(map(int,input().split()))

s,e = 0,n-1
mini = A[s]+A[e]
val = [A[s],A[e]]

while s < e:
    tmp = A[s]+A[e]
    
    if tmp == 0: # it's answer!
        val = [A[s],A[e]]
        break
    
    if abs(tmp) < abs(mini):
        mini = tmp
        val = [A[s],A[e]]
        
    if tmp > 0:
        e -= 1
    else:
        s += 1
        
print(' '.join(map(str,val)))