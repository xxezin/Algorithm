n = int(input())
D = [0]*1000001
pre = [0]*1000001

D[1],D[2],D[3] = 0,1,1
pre[1],pre[2],pre[3] = 0,1,1

for i in range(2,n+1):
    D[i] = D[i-1]+1 # 일단 1을 빼는 경우 저장
    pre[i] = i-1

    if i%2==0 and D[i] > D[i//2] +1:# 1을 빼는 경우보다 2로 나뉘는 경우가 더 효율적(최소 경로)인 경우 업데이트
        D[i] = D[i//2]+1
        pre[i] = i//2
    if i%3==0 and D[i] > D[i//3] +1:# 1을 빼는 경우보다 3로 나뉘는 경우가 더 효율적(최소 경로)인 경우 업데이트
        D[i] = D[i//3]+1
        pre[i] = i//3

cur = n
print(D[cur])
while True:
    print(cur,end=' ')
    if cur == 1:
        break
    cur = pre[cur]