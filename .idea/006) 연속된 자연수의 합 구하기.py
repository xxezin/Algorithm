## pseudo code ##
"""
n 변수 입력받기
변수 초기화 (count,sum,start_index,end_index = 1)

while end_index != n:
    if sum == n :
        count+=1
        end_index+=1
        sum+= end_index
    elif sum > n :
        sum-= start_index
        start_index+=1
    else :
        end_index+=1
        sum+= end_index

print(count)
"""

# code
n = int(input())
count,sum,start_index,end_index = 1,1,1,1

while end_index != n:
    if sum == n:
        count +=1
        end_index +=1
        sum +=end_index
    elif sum > n:
        sum -= start_index
        start_index +=1
    else:
        end_index +=1
        sum += end_index

print(count)