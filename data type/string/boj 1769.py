n = str(input())
cnt = 0
while True:
    if int(n) < 10:
        print(cnt)
        if int(n) in {3,6,9}:
            print("YES")
            break
        else:
            print("NO")
            break
    cnt += 1
    n = str(sum(list(map(int,n))))
    