def func(k):
    cache = [0 for idx in range(k+1)]
    for i in range(2,k+1):
        cache[i] = cache[i-1]+1
        if i%2==0:
            cache[i] = min(cache[i],cache[i//2]+1)
        if i%3==0:
            cache[i] = min(cache[i],cache[i//3]+1)

    return cache[k]

n = int(input())
print(func(n))