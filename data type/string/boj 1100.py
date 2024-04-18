answer = 0
for i in range(8):
    tmp = list(input().rstrip())
    if i%2 == 0:
        for j in range(0,8,2):
            if tmp[j] == "F":
                answer += 1
                
    else:
        for j in range(1,8,2):
            if tmp[j] == "F":
                answer += 1

print(answer)