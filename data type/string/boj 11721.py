s = input().rstrip()

i = 0
while i < len(s):
    if i+10 <= len(s):
        print(s[i:i+10])
        i += 10
    elif i < len(s) and i+10 > len(s):
        print(s[i:])
        break
