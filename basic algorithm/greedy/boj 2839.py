n = int(input())
cnt = 0
tmp = 0
if n >= 5:
    tmp = n//5

while tmp >= 0:
    if (n - tmp*5) %3 == 0:
        cnt = tmp + (n - tmp*5)//3
        break
    else:
        tmp -= 1
        
if cnt:
    print(cnt)
else:
    print(-1)