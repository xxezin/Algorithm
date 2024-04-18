s = input().rstrip()
A = [-1]*(26)

for idx,char in enumerate(s):
    if A[ord(char)-97] == -1:
        A[ord(char)-97] = idx
print(' '.join(map(str,A)))

def solution(s):
    answer = [-1]*(26)
    
    for idx,char in enumerate(s):
        if answer[ord(char)-97] == -1:
            answer[ord(char)-97] = idx
    return ' '.join(map(str,answer))