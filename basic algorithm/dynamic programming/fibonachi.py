# recursive call 활용
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


# dynamic programming 활용
def fibo_dp(n):
    cache = [0 for idx in range(n+1)] # memoization
    cache[0] = 0
    cache[1] = 1
    
    for idx in range(2,n+1):
        cache[idx] = cache[idx-1] + cache[idx-2]
    return cache[n]

print(fibo(2))
print(fibo_dp(2))