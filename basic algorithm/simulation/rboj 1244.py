import sys
input = sys.stdin.readline

s_cnt = int(input())
S = list(map(int,input().split()))
n = int(input())
for _ in range(n):
    sex,num = map(int,input().split())
    if sex == 1:
        for i in range(num-1,s_cnt,num):
            if S[i] == 1:
                S[i] = 0
            else:
                S[i] = 1
    elif sex == 2:
        if S[num-1]:
            S[num-1] = 0
        else:
            S[num-1] = 1
            
        i = 1
        while num-i >= 1 and num +i <= s_cnt:
            if S[num-1 -i] == S[num-1 +i]:
                if S[num-1 -i]:
                    S[num-1 -i],S[num-1 +i] = 0,0
                else:
                    S[num-1 -i],S[num-1 +i] = 1,1
                
            else:#다르면
                break
                
            i += 1

i = 0
while i != s_cnt:
    if i+20 < s_cnt:
        print(*S[i:i+20])
        i += 20
    else:
        print(*S[i:])
        break