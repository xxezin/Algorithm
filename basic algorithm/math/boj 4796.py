import sys
input = sys.stdin.readline

test = 0
while True:
    test += 1
    L,P,V = map(int,input().split())
    if L==0:
        break
    
    a,b = divmod(V,P)
    if b >= L:
        answer = a*L + L
    else:
        answer = a*L + b
        
    print(f'Case {test}: {answer}')