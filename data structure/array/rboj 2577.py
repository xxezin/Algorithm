a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
R = [0 for _ in range(10)]
for i in result:
    R[int(i)] += 1
    
print('\n'.join(map(str,R)))