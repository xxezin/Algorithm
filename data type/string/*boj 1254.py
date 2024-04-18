s = list(input().rstrip())
n = len(s) # 문자열 길이

for i in range(n):
    if s[i:] == s[i:][::-1]:
        print(n+i)
        break
