
used = [False]*10001

def selfnum(k):
    ans = 0
    ans += k

    tmp = list(str(k))
    for j in tmp:
        ans += int(j)

    if ans <= 10000 and not used[ans]:
        used[ans] = True
        selfnum(ans)
        return

for i in range(1,10000):
    if not used[i]:
        selfnum(i)

for i in range(1,10000):
    if not used[i]:
        print(i)
