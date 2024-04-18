import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = ""
    num, str = input().split()
    
    for s in str:
        answer += s*int(num)
    
    print(answer)