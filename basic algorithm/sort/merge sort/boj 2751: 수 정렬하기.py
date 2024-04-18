import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(arr):
    if len(arr)>1:
        m = len(arr)//2
        leftArr = arr[:m]
        rightArr = arr[m:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i = j = k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i+=1
            else:
                arr[k] = rightArr[j]
                j+=1
            k+=1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i+=1
            k+=1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j+=1
            k+=1



n = int(input())
A = [0]*n
for i in range(n):
    A[i] = int(input())

mergeSort(A)
for i in range(n):
    print(str(A[i])+'\n')