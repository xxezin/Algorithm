import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    answer = 0
    tmp = 0
    for i in s:
        if i == "O":
            tmp += 1
            answer += tmp
        else:
            tmp = 0
    print(answer)