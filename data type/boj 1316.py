import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    char = set()
    word = input().rstrip()
    
    for i in range(len(word)):
        if word[i] not in char:
            char.add(word[i])
            
        else:
            if word[i-1] != word[i]:
                break
            
    else:
        answer += 1

print(answer)