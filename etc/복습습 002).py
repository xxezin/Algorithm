n = int(input())
jumsoo = list(map(int,input().split()))
mymax = max(jumsoo)
sum = sum(jumsoo)

print(sum*100/n/mymax)