import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    tmp = list(map(int,input().split()))
    n = tmp[0]
    
    answer = 0
    for i in range(1,20):
        for j in range(i+1,21): # i 뒤에 애들과 전부 비교
            if tmp[i] > tmp[j]: # i가 더 크면
                tmp[i],tmp[j] = tmp[j],tmp[i] # 자리 바꿈
                answer += 1
    print(n,answer)