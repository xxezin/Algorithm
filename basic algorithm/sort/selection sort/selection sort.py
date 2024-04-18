# 첫번째 방법
def selectionSort(arr):
    for stp in range(len(arr)):
        min = stp # 일단 현재 선택한 인덱스를 최소로
        for i in range(stp+1, len(arr)): # 선택한 인덱스 다음부터
            if arr[i] < arr[min]:
                min = i
        
        arr[stp],arr[min] = arr[min],arr[stp]


# 두번째 방법
def selectionsSort2(arr):
    for stand in range(len(arr)-1):
        lowest = stand
        for index in range(stand+1,len(arr)):
            if arr[lowest] > arr[index]:
                lowest = index

        arr[stand],arr[lowest] = arr[lowest],arr[stand]