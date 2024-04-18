text = input()
alpha = [0 for _ in range(26)]

for i in text:
    alpha[ord(i)-ord('a')] += 1
    
print(*alpha)