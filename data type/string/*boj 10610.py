# 100000 개의 숫자로 구성되어 있음... 
# 30의 배수가 되는 가장 큰 수를 만들고 싶음 ... 
# 각 자리수의 합이 3으로 나눠 떨어지면 3의 배수

from itertools import permutations
n = list(map(int,input()))
n = sorted(n,reverse=True)

sum = 0
if 0 not in n:
    print(-1)
else:
    for i in n:
        sum += i
    if sum%3 != 0:
        print(-1)
    else:
        print("".join(map(str,n)))