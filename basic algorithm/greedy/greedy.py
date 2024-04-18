# 매 순간, 눈 앞에 보이는 것 중 최선의 선택을 하는 알고리즘
# 최적의 해에 가까운 값을 구하는 것. 최적의 해가 아닐 수 있음

## boj 11047 # 동전 0

import sys
input = sys.stdin.readline

def greedy(value, coin_list):
    tot_cnt = 0
    
    for coin in coin_list:
        cnt = value//coin
        tot_cnt += cnt
        value -= coin*cnt
        
    return tot_cnt


n,k = map(int,input().split()) # 동전의 개수, 지불 해야할 값
A = [int(input()) for _ in range(n)] # 동전의 가치
A.sort(reverse=True) # 동전의 가치가 큰 것부터 정렬

print(greedy(k,A))