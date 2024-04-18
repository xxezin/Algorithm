s = input().rstrip()
bomb = input().rstrip()
b = len(bomb)
ans = []

for i in s:
    ans.append(i)
    if bomb[-1] == ans[-1] and ''.join(ans[-b:])==bomb:
        del ans[-b:]

print(''.join(ans) if ans else 'FRULA')