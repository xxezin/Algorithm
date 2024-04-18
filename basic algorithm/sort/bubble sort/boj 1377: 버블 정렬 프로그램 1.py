# # n의 최대 범위가 500,000으로 버블 정렬로 풀었더니 시간초과됨
# import sys
# input = sys.stdin.readline

# def bubblesort(array):
#     for i in range(len(array)-1):
#         change = False
#         for j in range(len(array)-1-i):
#             if array[j] > array[j+1]:
#                 change = True
#                 array[j],array[j+1] = array[j+1],array[j]
        
#         if not change:
#             return i+1

# n = int(input())
# A = [0]*n
# for i in range(n):
#     A[i] = int(input())

# ans = bubblesort(A)
# print(ans)



# 가장 많이 이동한 숫자의 인덱스 차이로 답을 알 수 있음...
import sys
input = sys.stdin.readline

def solution(array):
    global Max
    for i in range(len(array)):
        if Max < array[i][1] - i:
            Max = array[i][1]-i

    return Max+1


n = int(input())
A = [0]*n
for i in range(n):
    A[i] = (int(input()),i)

Max = 0
sorted_A = sorted(A) # sorted로 정렬

ans = solution(sorted_A)
print(ans)