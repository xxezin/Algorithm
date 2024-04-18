T = int(input())
answer = list(input().rstrip())
for _ in range(T-1):
    tmp = list(input().rstrip())
    for i in range(len(tmp)):
        if answer[i] != tmp[i]:
            answer[i] = "?"
print(''.join(answer))