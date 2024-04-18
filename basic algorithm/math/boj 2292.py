n = int(input())

beol = 1
cnt = 1
while n > beol:
    beol += 6*cnt
    cnt += 1
print(cnt)