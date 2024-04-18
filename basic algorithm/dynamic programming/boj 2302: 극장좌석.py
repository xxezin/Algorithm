# 총 좌석 개수 N개 (1<=N<=40)
# 고정 좌석 개수 M개 (0<=M<=N)
# 고정석의 번호가 작은 수부터 큰 수의 순서로 한 줄에 하나씩 입력됨

# 고정석을 기준으로 자기네들 끼리 두개씩만 자리 바꾸기 가능...
# D = 연속된 수 개수?
# 1 =>1 총 1
# 2 =>2 총 2
# 3 =>3 총 3
# 4 => 1234 2134 2143 1243 1324 총 5
# 5 => 총 8
# 12345 13245 12354 12435 21435
# 21345 13254 21354 
# 6 => 123456 123465 124356 124365 123546 
# 213456 213465 214356 214365 213546
# 132456 132465 132546

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

VIP = [] # VIP 인덱스 저장
for _ in range(m):
    VIP.append(int(input()))

R = [1]*41
R[1] = 1
R[2] = 2

for i in range(3,41):
    R[i] = R[i-1]+R[i-2]

ans =1
if m>=1:
    pre = 0
    for i in range(m):
        ans *= R[VIP[i]-1-pre]
        pre = VIP[i]
    ans *= R[n-pre]

else:
    ans = R[n]

print(ans)

    # if D[i] != -1: # VIP 좌석이 아니면
    #     D[i] = D[i-1]+1 # 연속된 길이 +1
    #     if i==n-1:
    #         ans.append(D[i])
    # elif D[i] == -1: # VIP 좌석이면
    #     ans.append(D[i-1])
