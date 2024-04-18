# 정렬할 데이터 N개
# 정렬할 리스트 A
# for i in range(데이터길이 -1):
#     for j in range(데이터길이 -1 -i):
#         if 앞 데이터 > 뒤 데이터: 
#             swap(앞 데이터, 뒤 데이터)
#             한번도 swap 안되면 그냥 탈출

# 버블 정렬
def bubblesort(data):
    for i in range(len(data)-1): # 턴 수
        swap = False
        for j in range(len(data)-1-i): # 데이터 인덱스
            if data[j] > data[j+1]:
                data[j+1],data[j] = data[j], data[j+1]
                swap = True

        if not swap:
            break

import random

data_list = random.sample(range(100),50)
bubblesort(data_list)
print(data_list)



# 다시 한번 작성해보는 연습
def bubblesort(array):
    for i in range(0,len(array)-1): # 턴 수
        swap = False
        for j in range(0,len(array)-1-i): # 조사하는 인덱스 번호
            if array[j] > array[j+1]: # 앞 수가 뒷 수보다 크면
                array[j],array[j+1] = array[j+1],array[j]
                swap = True
        
        if not swap : # 한 텀을 돌았는데, swap한 적이 없으면
            break


