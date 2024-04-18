n = int(input())
dis = list(map(int,input().split()))
cost = list(map(int,input().split()))

min_price = cost[0]
answer = 0
for i in range(len(cost)-1):        
    min_price = min(min_price,cost[i])
    answer += min_price * dis[i]
    
print(answer)