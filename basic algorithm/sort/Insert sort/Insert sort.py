# 첫번째 방법
def insertionSort(arr):
    for i in range(1, len(arr)): # 턴 수
        tmp = arr[i]
        j = i - 1
         
        while j >= 0 and tmp < arr[j]: # 그 앞의 숫자들이랑 다 비교해봄
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = tmp
    return arr


# 두번째 방법
def insertionSort2(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
    
    return arr


