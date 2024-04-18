s = str(input())

A = []
for i in range(len(s)):
    A.append(s[i::])

print('\n'.join(sorted(A)))