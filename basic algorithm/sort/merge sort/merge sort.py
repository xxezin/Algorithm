def mergeSort(arr):
    if len(arr) > 1: # 배열 길이가 1보다 크면
        r = len(arr)//2 # 쪼개
        leftArr = arr[:r] # 쪼개진 왼쪽 배열
        rightArr = arr[r:] # 쪼개진 오른쪽 배열

        mergeSort(leftArr) # 왼쪽 그룹에 대해서 반복
        mergeSort(rightArr) # 오른쪽 그룹에 대해서 반복

        i = j = k = 0
       
        while i < len(leftArr) and j < len(rightArr): 
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
       
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1