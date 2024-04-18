n = int(input())

s,e,cnt = 1,1,1
sum = 1
while e != n:
    if sum == n:
        cnt += 1
        e += 1
        sum += e
    elif sum > n:
        sum -= s
        s += 1
    else:
        e += 1
        sum += e

print(cnt)