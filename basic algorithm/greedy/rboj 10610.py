n = input()
if n.count('0') >= 1:
    n = sorted(n,reverse=True)
    if sum(map(int,n)) %3 == 0:
        print(''.join(n))
    else:
        print(-1)
else:
    print(-1)