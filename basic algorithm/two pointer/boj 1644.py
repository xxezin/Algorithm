import math
n = int(input())
A = [0]*(n+1)
for i in range(2,n+1):
    A[i] = i
    
for i in range(2,int(math.sqrt(n+1))+1): # 제곱근까지
    if A[i] == 0:
        continue
    
    for j in range(i+i,n+1,i):
        A[j] = 0

# 소수 누적합 리스트
B = [0]
sum = 0
for i in range(2,n+1):
    if A[i]:
        sum += A[i]
        B.append(sum)
        
l,r,cnt = 0,1,0
while r < len(B):
    tmp = B[r] - B[l]
    if tmp == n:
        cnt += 1
        l += 1
    elif tmp > n:
        l += 1
    else:
        r += 1
        
print(cnt)