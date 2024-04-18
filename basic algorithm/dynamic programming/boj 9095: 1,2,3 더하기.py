import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    cache = [0 for idx in range(n+1)]

    for j in range(1,n+1):
        if j==1:
            cache[1] = 1
        elif j==2:
            cache[2] = 2
        elif j==3:
            cache[3] = 4
        else:
            cache[j] = cache[j-1]+cache[j-2]+cache[j-3]
    
    print(cache[n])