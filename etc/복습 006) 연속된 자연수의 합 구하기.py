N = int(input())
count = 1
start = 1
end = 1
sum = 1

while end != N :
    if sum == N:
        count +=1
        end +=1
        sum += end
    elif sum > N:
        sum -= start
        start +=1
    else :
        end +=1
        sum += end

print(count)

