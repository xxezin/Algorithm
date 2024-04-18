def insertSort(arr):
    for i in range(1,len(arr)):
        tmp = arr[i]
        j = i-1
        while j >=0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        
        arr[j+1] = tmp

n = int(input())
A = list(map(int,input().split()))
sum = [0]*n

insertSort(A)
sum[0] = A[0]
for i in range(1,n):
    sum[i] = sum[i-1] + A[i]

ans = 0

for i in range(n):
    ans += sum[i]

print(ans)