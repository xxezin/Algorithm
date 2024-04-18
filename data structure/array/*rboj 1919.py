a = input()
b = input()

result = 0
for i in range(ord('a'),ord('z')+1):
    result += abs(a.count(chr(i))-b.count(chr(i)))

print(result)